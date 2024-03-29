import os
import pickle
import hashlib


R2S_BASE_FOLDER = '/home/mnf/projects/phd/r2s/'
R2S_UTIL = R2S_BASE_FOLDER + 'src/util/'
R2S_CACHE = R2S_UTIL + 'temp/cache/'
R2S_CACHEMAP = R2S_CACHE + 'cachemap.pickle'



def _get_args_dict(fn, args, kwargs):
    
    args_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
    key =  {**dict(zip(args_names, args)), **kwargs}
    key['self'] = str(type(key['self']))
    if 'use_cache' in key:
        if key['use_cache'] == False: ##if this is False it disables the cache 
            key = {}

    metadata = {}
    return key, metadata

def cached():
    """
    A function that creates a decorator which will use "cachefile" for caching the results of the decorated function "fn".
    """
    def decorator(fn):  # define a decorator for a function "fn"
        def wrapped(*args, **kwargs):   # define a wrapper that will finally call "fn" with all arguments            
            # if cache exists -> load it and return its content
            
            key, metadata = _get_args_dict(fn, args, kwargs)   

            if key == {}:
                return fn(*args, **kwargs)
            
            hashkey = hashlib.sha1(str(key).encode("utf-8")).hexdigest()
            cachemap = open_cachemap(R2S_CACHEMAP)

            print(key)
           
            if hashkey in cachemap:
                if os.path.exists(cachemap[hashkey]):
                        with open(cachemap[hashkey], 'rb') as cachehandle:
                            print("using cached result from '%s'" % cachemap[hashkey])
                            return pickle.load(cachehandle)

            # execute the function with all arguments passed
            res = fn(*args, **kwargs)
        
            cachemap[hashkey] = R2S_CACHE + hashkey + '.pickle'

            res['metadata'] = metadata 
            res['metadata']['cache'] = cachemap[hashkey]

            ## update cache map
            update_cachemap(R2S_CACHEMAP,hashkey,cachemap[hashkey])

            # write to cache file
            with open(cachemap[hashkey], 'wb') as cachehandle:
                print("saving result to cache '%s'" % cachemap[hashkey])
                pickle.dump(res, cachehandle, protocol=pickle.HIGHEST_PROTOCOL)


            return res

        return wrapped

    return decorator   # return this "customized" decorator that uses "cachefile"

def open_cachemap(p):
    cachemap = {}
    if os.path.exists(p):
        with open(p, 'rb') as cachehandle:
            cachemap = pickle.load(cachehandle)
    
    return cachemap

def update_cachemap(p,k,v):

    cachemap = open_cachemap(p)
    cachemap[k] = v
    with open(p, 'wb') as cachehandle:
        pickle.dump(cachemap, cachehandle, protocol=pickle.HIGHEST_PROTOCOL)

def set_hyperparams(self, hyperparams, allparameters):

    #_VALID_KEYWORDS = {'users', 'n', 'nnbrs'}
    self.hyperparam = {}
    for keyword, value in allparameters._get_kwargs():
        if keyword in hyperparams:
            self.hyperparam[keyword] = value
     