#!/usr/bin/env python
# coding: utf-8

# In[5]:


#importing random module
import random

#List of story inputs

Time = ['Once Upon a time', 'A hundred years ago', 'Long before the modern world was created']
Subject = ['a King', 'a mighty girl', 'the long footed giants', 'a group of friends']
Place = ['a lonely palace', 'a dense forest', 'the mountains', 'the underworld beneath the sea']

#Selecting an item from each list and concatenating them
print(random.choice(Time) + ' ' + random.choice(Subject) + ' lived in ' + random.choice(Place))





