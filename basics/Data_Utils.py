
# coding: utf-8

# # Data Utilities

# This notebook contains utility functions for data manipulation and generation needed for NN Curriculum code

# In[3]:


import math
from sklearn.datasets import make_moons


# In[1]:


def get_spiral(radius, step, resolution=.1, angle=0.0, start=0.0):
    dist = start+0.0
    coords=[]
    while dist*math.hypot(math.cos(angle),math.sin(angle))<radius:
        cord=[]
        cord.append(dist*math.cos(angle))
        cord.append(dist*math.sin(angle))
        coords.append(np.array(cord))
        dist+=step
        angle+=resolution
    return (np.array(coords))


# In[4]:


def get_moons(samples = 100, noise = 0.05):
    return (np.array(make_moons(n_samples = samples, noise = noise)))


# In[ ]:


print('Data Utilities Imported !')

