#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = input()
numbers = string.split()
numbers = list(map(int, numbers))
result = []
for e in numbers:
    if e < 10:
        result.append(e)
for e in result:
    print(e, end=" ")


# In[ ]:




