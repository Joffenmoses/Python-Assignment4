#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment 1
text='What we think we became; we are Python programmers'
count=text.count('we')
addstep=0
ntext=0
check=0
flag=True
while flag:
    ftext=text.find('we')
    ntext=ntext+ftext+addstep
    print(ntext)
    text=text[ftext+1:]
    addstep+=1
    check+=1
    if count==check:
        flag=False


# In[29]:


t1='What we think we became we are Python programmers'
t2='letsupgrage'
t3='LETSUPGRADE'
print(t1.islower())
print(t2.islower())
print(t3.islower())
print(t1.isupper())
print(t2.isupper())
print(t3.isupper())


# In[ ]:




