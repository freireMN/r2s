import sys, time
from argparse import Namespace

R2S_BASE_FOLDER = '/home/mnf/projects/phd/r2s/'
R2S_UTIL = R2S_BASE_FOLDER + 'src/util/'

R2S_DATASET_FOLDER_IN  = R2S_BASE_FOLDER + 'data/ml-latest-small'
R2S_DATASET_FOLDER_OUT = R2S_BASE_FOLDER + 'data/R2SDatasets/movielens-small' 
R2S_IMPORT_DATASET_MESSAGE = 'Time elapsed {} to run {} algorithm '

sys.path.append(R2S_UTIL)

import dataset_import as r2sdata

args = Namespace(folderIn=R2S_DATASET_FOLDER_IN, folderOut=R2S_DATASET_FOLDER_OUT,extension='csv')

ts = time.time()
ret = r2sdata.import_dataset(args)
te = time.time()

print(R2S_IMPORT_DATASET_MESSAGE.format(te-ts, ret))
    