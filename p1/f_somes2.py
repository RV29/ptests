#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from .f_somes import p_exp

def adder(x,y):
    return x+y

def multer(x,y,n):
    return p_exp( np.log(x,n) + np.log(y,n) )

