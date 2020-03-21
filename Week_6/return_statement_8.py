#!/usr/bin/env python
# coding: utf-8

# In[2]:


def format_string(string):
    lst = string.split()
    return f'Name: {lst[0]}. Surname: {lst[1]}. Age: {lst[2]}.'
string = input()
result = format_string(string)
print(result)


# In[ ]:




