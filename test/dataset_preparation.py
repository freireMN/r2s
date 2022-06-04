import sys, time
from argparse import Namespace


hardpath = '/home/vagrant/repo/r2s/'
sys.path.append(hardpath + 'src/util/')

import dataset_import as r2sdata

args = Namespace(folderIn='/source/datasets/movielens/ml-latest-small'
                ,folderOut=hardpath + 'data/R2SDatasets/movielens-small'
                ,extension='csv')


ts = time.time()
ret = r2sdata.import_dataset(args)

te = time.time()



print ('Time elapsed {} to run {} algorithm '.format(te-ts, ret) )
    