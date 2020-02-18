#!/usr/bin/env python
# coding: utf-8

# In[6]:


string1 = input()
string2 = input()
numbers1 = string1.split()
numbers2 = string2.split()
result = []
for e1 in numbers1:
    for e2 in numbers2:
        if e1 == e2:
            result.append(e1)
            break
intersection = tuple(list(map(int, result)))
print(intersection)


# In[ ]:




