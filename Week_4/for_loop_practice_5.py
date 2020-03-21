#!/usr/bin/env python
# coding: utf-8

# In[5]:


string = input()
info = string.split()
info.sort(reverse=True)
for e in info:
    print(e, end=" ")


# In[ ]:




