#!/usr/bin/env python
# coding: utf-8

# In[32]:


n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    a1 = 0
    a2 = 1
    i = 2
    while i <= n:
        fn = a1 + a2
        a1 = a2
        a2 = fn
        i += 1
    print(fn)


# In[ ]:




