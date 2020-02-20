#!/usr/bin/env python
# coding: utf-8

# In[2]:


numbers1 = input().split()
numbers2 = input().split()
intersection = tuple(map(int, [x for x in numbers1 if x in numbers2]))
print(intersection)


# In[ ]:




