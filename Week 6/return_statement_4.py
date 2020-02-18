#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ordered(lst1, lst2):
    lst3 = lst1+lst2
    lst3.sort()
    return lst3
lst1 = list(input())
lst2 = list(input())
lst3 = ordered(lst1, lst2)
for e in lst3:
    print(e, end="")


# In[ ]:




