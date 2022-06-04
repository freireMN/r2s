import sys, time
import argparse 
from argparse import Namespace


hardpath = '/home/vagrant/repo/r2s/'

sys.path.append(hardpath + 'src/util/')
sys.path.append(hardpath + 'src/modules/')
sys.path.append(hardpath + 'src/modules/rec')
sys.path.append(hardpath + 'src/modules/rec/algo')



#sys.path.append('/source/R2S/src/environment/recommender/algorithms')
#sys.path.append('/source/R2S/src/util')


import R2SObject


parser=argparse.ArgumentParser()


p = argparse.Namespace(dataset={'name':'MovieLens', 'path': hardpath +  'data/R2SDatasets/movielens-small'}
                    , data={'ratings':None, 'movies': None} #TODO: specify the columns to load to avoid loading the whole file
                    , matrix={'source':'ratings', 'row':'userId', 'col':'movieId', 'data':'rating'} #format to allow algo computations (on env load ?!?)
                    , algo={ 'Random':'basic'
                           ,'PopScore': 'basic'
                           , 'R2SWrapper_ItemItem':'collaborative_ItemItem'
                           , 'R2SWrapper_UserUser':'collaborative_UserUser'
                           , 'R2SWrapper_FunkSVD':'funksvd'
                           } #list of avalilable algos ---- each env. does not need to have all algos .... 

                    , algodata={'Random':{'items':{'dataset':'movies', 'feature':'movieId'}}  # especific to each algo .... 
                               ,'PopScore':{'scores':{'dataset':'ratings','feature':'movieId'}}
                               ,'R2SWrapper_ItemItem':{'ratings':['userId']}
                               ,'R2SWrapper_UserUser':{'ratings':['userId']}
                               ,'R2SWrapper_FunkSVD':{'ratings':['userId']}
                               
                               })

R2SEnv = R2SObject.R2S(p)

#action = argparse.Namespace(algo = 'R2SWrapper_ItemItem')
#parameters = argparse.Namespace(users = [25], n = 3, nnbrs = 3, save_nbrs=3)


#action = argparse.Namespace(algo = 'R2SWrapper_UserUser')
#parameters = argparse.Namespace(users = [25], n = 3, nnbrs = 3, save_nbrs=3)


action = argparse.Namespace(algo = 'R2SWrapper_FunkSVD')   
parameters = argparse.Namespace(users = [25], n = 3, features = 50)
    

ts = time.time()
ret = R2SEnv.algo[action.algo].recommend(parameters)
te = time.time()

print(ret)

print ('Time elapsed {} to run {} algorithm '.format(te-ts, action.algo) )
    