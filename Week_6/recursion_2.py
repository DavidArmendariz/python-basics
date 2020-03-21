#!/usr/bin/env python
# coding: utf-8

# In[8]:


def sum_of_digits(n):
    if n >= 0 and n <= 9:
        return n
    else:
        return n%10 + sum_of_digits(n//10)
number = int(input())
print(sum_of_digits(number))


# In[ ]:




