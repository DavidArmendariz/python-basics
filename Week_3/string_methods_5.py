#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = input()
result = ""
for i in range(len(string)):
    if i == len(string)-1:
        result += string[0]
    else:
        result += string[i+1]
print(result)


# In[ ]:




