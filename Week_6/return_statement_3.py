#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_quarter(month):
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    elif month >= 10 and month <= 12:
        return 4
number = int(input())
print(get_quarter(number))


# In[ ]:




