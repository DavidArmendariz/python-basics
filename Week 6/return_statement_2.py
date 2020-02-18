#!/usr/bin/env python
# coding: utf-8

# In[7]:


def isprime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
number = int(input())
if isprime(number):
    print('YES')
else:
    print('NO')


# In[ ]:




