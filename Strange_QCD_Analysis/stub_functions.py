#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
topdir = os.getcwd()
loopsubdir = topdir + "\\exported_data\\loop"


# In[9]:


import numpy as np


# In[43]:


def jackknife_var_resample(original_data):
    """Jackknife resample a data list and return the variance"""
    
    import numpy as np
    
    n = np.shape(original_data)[0]
    resamples = np.empty([n,n-1])
    jackknifed_list = np.empty(n)
    mean = np.mean(original_data)
    var_sum = 0
    
    for i in range(n):
        resamples[i] = np.delete(original_data,i)
        jackknifed_list[i] = resamples[i].mean()
        var_sum = var_sum + np.square((jackknifed_list[i]-mean))
    
    variance = 1/(n*(n-1)) * var_sum

    #print(jackknifed_list.mean())
    #print(variance)
    return(variance)


# In[4]:


def loop_read(loopASCII):
    """Read loop ASCII file and convert to dataframe"""
    
    nt = 64;
    ns = 24;
    iters = 4000;
    
    
    
    return loop_data


# In[ ]:


def strange_read(nucleonASCII):
    """Read strange ASCII file and convert to dataframe"""
    
    nt = 64;
    ns = 24;
    iters = 4000;
    
    
    
    return nucleon_data


# In[ ]:


def three_point(nucleon_data, loop_data):
    """Calculate 3-point correlator"""
    
    
    
    return

