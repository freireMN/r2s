
import sys

from cache import cached, set_hyperparams
from lenskit.algorithms import user_knn


class R2SWrapper_UserUser():

    def __init__(self, parent):
        algodata = parent.algodata[repr(self)]
        self.ui_coo = parent.ui_coo
        self.ratings = parent.__dict__['data']['ratings'][['userId','movieId','rating']]
        self.ratings.columns =['user','item','rating']
    
    @cached()
    def fit(self, hyperparams):
        
        trained_data = self._train_model(10) # 
        self.ItemItem = trained_data['self']

        rec = {}
        rec['metadata'] = trained_data['metadata']

        for u  in self.hyperparam['users']:

            prediction = self.ItemItem.predict_for_user(u,self.ui_coo.col) 
            rec[str(u)] = prediction.nlargest(self.hyperparam['n']).index.tolist() 

        return rec

    @cached()
    def _train_model(self, size):
        return {'self': self.UserUser.fit(self.ratings)}


    def recommend(self, parameters):

       
        set_hyperparams(self, {'users', 'n', 'nnbrs'}, parameters)
        self.UserUser = user_knn.UserUser(self.hyperparam['nnbrs'])
        self.rec = self.fit(self.hyperparam)
        return self.rec
  

    def __str__(self):
        return 'UserUser - Knn algo for UserUser'

    def __repr__(self):
        return 'R2SWrapper_UserUser'
