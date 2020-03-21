#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calc(a, b, operation):
    if operation == '+':
        return a+b
    elif operation == '*':
        return a*b
    elif operation == '-':
        return a-b
    elif operation == '/':
        return a/b

a = float(input())
b = float(input())
operation = input()
print(calc(a, b, operation))


# In[ ]:




