#!/usr/bin/env python
# coding: utf-8

# In[11]:


def area(w, h):
    return w*h
def perimeter(w, h):
    return 2*w+2*h
numbers = input().split()
w,h = list(map(int, numbers)) 
print('Area:', int(area(w, h)))
print('Perimeter:', int(perimeter(w, h)))


# In[ ]:




