#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_strings(lst):
    lst = lst.split()
    lst = list(map(int, lst))
    return sum(lst)
string = input()
print(sum_strings(string))


# In[ ]:




