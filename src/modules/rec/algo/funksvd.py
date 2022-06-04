
import sys

from cache import cached, set_hyperparams
from lenskit.algorithms import funksvd


class R2SWrapper_FunkSVD():

    
    def __init__(self, parent):

        algodata = parent.algodata[repr(self)]
        self.ui_coo = parent.ui_coo
        self.ratings = parent.__dict__['data']['ratings'][['userId','movieId','rating']]
        self.ratings.columns =['user','item','rating']
    

    @cached()
    def fit(self, hyperparams):
        
        trained_data = self._train_model(10) # 
        self.FunkSVD = trained_data['self']

        rec = {}
        rec['metadata'] = trained_data['metadata']

        for u  in self.hyperparam['users']:

            prediction = self.FunkSVD.predict_for_user(u,self.ui_coo.col) 
            rec[str(u)] = prediction.nlargest(self.hyperparam['n']).index.tolist() 

        return rec

    @cached()
    def _train_model(self, size):
        return {'self': self.FunkSVD.fit(self.ratings)}


    def recommend(self, parameters):

       
        set_hyperparams(self, {'users', 'n', 'features'}, parameters)
        self.FunkSVD = funksvd.FunkSVD(self.hyperparam['features'])
        self.rec = self.fit(self.hyperparam)
        return self.rec


    def __str__(self):
        return 'FunkSVD - a complex algo'

    def __repr__(self):
        return 'R2SWrapper_FunkSVD'
