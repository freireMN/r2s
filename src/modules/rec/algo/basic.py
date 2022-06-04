
# extracted and adapted from Lenskit for R2S purposes
""" 
    basic.py
    

"""

#AlgoParam = Enum('score_method', 'quantile rank count')


import pandas as pd
import numpy as np
import scipy.sparse as spa
import pickle
import os.path
import sys

from datetime import datetime

#sys.path.append('/source/R2S/src/util')

from cache import cached, set_hyperparams
#from R2Sprofile import profileit




class PopScore():
    
    def __init__(self, parent):

        algodata = parent.algodata[repr(self)]
        self.ui_coo = parent.ui_coo
        self.scores = parent.__dict__['data'][algodata['scores']['dataset']][algodata['scores']['feature']].value_counts() 

    def fit_by_quantile(self):
        print('by quantile')
        cmass = self.scores.sort_values()
        cmass = cmass.cumsum()
        cdens = cmass / self.scores.sum()
        return cdens.sort_index()

    def fit_by_rank(self):
        print('by rank')
        return self.scores.rank().sort_index()

    def fit_by_count(self):
        print('by count')
        return self.scores.sort_index()

    @cached()
    def fit(self, hyperparams):

        items = None
        rec = {}
        if hyperparams['score_method'] == 'quantile':
            items = self.fit_by_quantile()
        if hyperparams['score_method'] == 'rank':
            items = self.fit_by_rank()
        if hyperparams['score_method'] == 'count':
            items = self.fit_by_count()

        poplist = items.sort_values(ascending=False).index[:hyperparams['n']].to_numpy()
        for u in hyperparams['users']:
            rec[str(u)] = poplist
        return rec



        
    #@profileit
    def recommend(self, parameters):


        set_hyperparams(self, {'users', 'n', 'score_method'}, parameters)
        
        if self.hyperparam['users'] is None:
            self.hyperparam['users'] = np.unique(self.ui_coo.row)
        else:
            if len(self.hyperparam['users']) == 0:
                self.hyperparam['users'] = np.unique(self.ui_coo.row)

        self.rec = self.fit(self.hyperparam)
        return self.rec

    
    def __str__(self):
        return 'PopScore - A popularity algorithm'

    def __repr__(self):
        return 'PopScore'



class Random():

    def __init__(self, parent):
        

        algodata = parent.algodata[repr(self)]
        self.ui_coo = parent.ui_coo
        self.items = parent.__dict__['data'][algodata['items']['dataset']][algodata['items']['feature']].to_numpy()
        self.rec = None
        

    @cached()
    def fit(self, hyperparams):
        
        self.lil = self.ui_coo.tolil()
        rng = np.random.default_rng(1)
        rec = {}
        for i ,rated in zip(self.hyperparam['users'], self.lil.rows[tuple([self.hyperparam['users']])]):
            candidates = np.setdiff1d(self.items, rated, True)
            rec[str(i)] = rng.choice(candidates, self.hyperparam['n'], False)   

        return rec

    #@profileit
    def recommend(self, parameters):

        set_hyperparams(self, {'users', 'n'}, parameters)
      

        if self.hyperparam['users'] is None:
            self.hyperparam['users'] = np.unique(self.ui_coo.row)
        else:
            if len(self.hyperparam['users']) == 0:
                self.hyperparam['users'] = np.unique(self.ui_coo.row)

        self.rec = self.fit(self.hyperparam)

        return self.rec

    def __str__(self):
        return 'Random - A random algorithm'

    def __repr__(self):
        return 'Random'



""" TODO: avoid these classes from being instantiated outside the R2S scope
import inspect

def get_class_from_frame(fr):
  args, _, _, value_dict = inspect.getargvalues(fr)
  # we check the first parameter for the frame function is
  # named 'self'
  if len(args) and args[0] == 'self':
    # in that case, 'self' will be referenced in value_dict
    instance = value_dict.get('self', None)
    if instance:
      # return its class
      caller = getattr(instance, '__class__', None)
      print(type(caller))
      if  caller != '''<class 'R2SObject.R2S'>''':
          print('here')
          raise ValueError('This class cannot be instantiated by {}'.format(caller))
          raise SystemExit
          sys.exit()

      return getattr(instance, '__class__', None)
  # return None otherwise
  return None

"""