#!/usr/bin/env python
# coding: utf-8

# In[51]:


from math import floor
def convert_time(timestamp):
    h = floor(timestamp*(1/3600))
    m = floor((timestamp - h*3600)/60)
    s = timestamp - h*3600 - 60*m
    h, m, s = str(h), str(m), str(s)
    if len(str(h)) == 1:
        h = '0' + h
    if len(str(m)) == 1:
        m = '0' + m
    if len(str(s)) == 1:
        s = '0' + s
    return h+':'+m+':'+s
seconds = int(input())
result = convert_time(seconds)
print(result)


# In[ ]:




