#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = input()
result = ""
for ch in string:
    if not ch.isdigit():
        result += ch
print(result)


# In[ ]:




