#!/usr/bin/env python
# coding: utf-8

# In[12]:


reversed_number = ""
def reverse_number(n):
    global reversed_number
    if n > 0:
        reversed_number += str(n%10)
        reverse_number(n // 10)
    return int(reversed_number)
number = int(input())
print(reverse_number(number))


# In[ ]:




