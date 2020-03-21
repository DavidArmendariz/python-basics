#!/usr/bin/env python
# coding: utf-8

# In[7]:


def isprime(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True
x = [(i,'prime') if isprime(i) == True else i for i in range(10,51)]
print(x)


# In[ ]:




