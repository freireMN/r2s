import sys, time
import argparse 
from argparse import Namespace


R2S_BASE_FOLDER = '/home/mnf/projects/phd/r2s/'

R2S_UTIL = R2S_BASE_FOLDER + 'src/util/'
R2S_MODULES = R2S_BASE_FOLDER + 'src/modules/'
R2S_REC_FOLDER = R2S_MODULES + '/rec'
R2S_ALGO_FOLDER = R2S_REC_FOLDER + '/algo'
R2S_DATASET_FOLDER = R2S_BASE_FOLDER +  'data/R2SDatasets/movielens-small'


sys.path.append(R2S_UTIL)
sys.path.append(R2S_MODULES)
sys.path.append(R2S_REC_FOLDER)
sys.path.append(R2S_ALGO_FOLDER)


import R2SObject


parser=argparse.ArgumentParser()


p = argparse.Namespace(dataset={'name':'MovieLens', 'path': R2S_DATASET_FOLDER}
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



action = argparse.Namespace(algo = 'Random')
parameters = argparse.Namespace(users = [25], n = 3)

ts = time.time()
ret = R2SEnv.algo[action.algo].recommend(parameters)
te = time.time()


print(ret)
print ('Time elapsed {} to run {} algorithm '.format(te-ts, action.algo) )


action = argparse.Namespace(algo = 'PopScore')
parameters = argparse.Namespace(users = [25], n = 3, score_method='quantile')

ts = time.time()
ret = R2SEnv.algo[action.algo].recommend(parameters)
te = time.time()


print(ret)
print ('Time elapsed {} to run {} algorithm '.format(te-ts, action.algo) )



action = argparse.Namespace(algo = 'R2SWrapper_ItemItem')
parameters = argparse.Namespace(users = [25], n = 3, nnbrs = 3, save_nbrs=3)

ts = time.time()
ret = R2SEnv.algo[action.algo].recommend(parameters)
te = time.time()


print(ret)
print ('Time elapsed {} to run {} algorithm '.format(te-ts, action.algo) )


action = argparse.Namespace(algo = 'R2SWrapper_UserUser')
parameters = argparse.Namespace(users = [25], n = 3, nnbrs = 3, save_nbrs=3)

ts = time.time()
ret = R2SEnv.algo[action.algo].recommend(parameters)
te = time.time()


print(ret)
print ('Time elapsed {} to run {} algorithm '.format(te-ts, action.algo) )

action = argparse.Namespace(algo = 'R2SWrapper_FunkSVD')   
parameters = argparse.Namespace(users = [25], n = 3, features = 50)
   

ts = time.time()
ret = R2SEnv.algo[action.algo].recommend(parameters)
te = time.time()

print(ret)
print ('Time elapsed {} to run {} algorithm '.format(te-ts, action.algo) )
    