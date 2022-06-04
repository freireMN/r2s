# parameter space 

environment_setup = 
    {
    algo: [
     
            {
            'name':  'PopScore',
            'parameters': 
                [
                    {'score_method' : {'type':'discret', 'domain': {['quantile','rank','count']}   , 'default':'count', 'help':'link to somewhere'},
                    {'n'            : {'type':'numeric', 'domain' : {'min': 1, 'max':10, 'step': 1}, 'default':5      , 'help':'link to somewhere'}
                ]
            },
            {
            'name':  'Random',
            'parameters': 
                [
                    {'n'            : {'type':'numeric', 'domain' : {'min': 1, 'max':10, 'step': 1}, 'default':5      , 'help':'link to somewhere'}
                ]
            },
            {
            'name':  'R2SWrapper_ItemItem',
            'parameters': 
                [
                    {'n'            : {'type':'numeric', 'domain' : {'min': 1, 'max':10, 'step': 1}, 'default':5      , 'help':'link to somewhere'}
                    {'nnbrs'        : {'type':'numeric', 'domain' : {'min': 1, 'max':10, 'step': 1}, 'default':5      , 'help':'link to somewhere'}

                ]
            },
            {
            'name':  'R2SWrapper_UserUser',
            'parameters': 
                [
                    {'n'            : {'type':'numeric', 'domain' : {'min': 1, 'max':10, 'step': 1}, 'default':5      , 'help':'link to somewhere'}
                    {'nnbrs'        : {'type':'numeric', 'domain' : {'min': 1, 'max':10, 'step': 1}, 'default':5      , 'help':'link to somewhere'}

                ]
            },
            {
            'name':  'R2SWrapper_FunkSVD',
            'parameters': 
                [
                    {'n'            : {'type':'numeric', 'domain' : {'min': 1, 'max':10, 'step': 1}, 'default':5      , 'help':'link to somewhere'}
                    {'features'     : {'type':'numeric', 'domain' : {'min': 10, 'max':100, 'step': 1}, 'default':50   , 'help':'link to somewhere'}

                ]
            },
        ]
    }   
