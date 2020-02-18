#!/usr/bin/env python
# coding: utf-8

# In[11]:


string1 = input()
string2 = input()
numbers1 = string1.split()
numbers2 = string2.split()
result = []
for n1 in numbers1:
    if n1 in numbers2:
        result.append(n1)
        continue
if result:
    for e in result:
        print(e, end=" ")
else:
    print(" ")


# In[ ]:




