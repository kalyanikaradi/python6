#!/usr/bin/env python
# coding: utf-8

# In[2]:


#set
myset={2,3,4,5,6,7,8,9}


# In[3]:


myset


# In[6]:


myset1={4,7,8,2,8,9,10}


# In[7]:


myset1
#no repeated values


# In[8]:


myset2={2.34,5.7,4.78}


# In[9]:


myset2


# In[10]:


myset3={'abc','xyz','pqr','pqr'}


# In[11]:


myset3


# In[13]:


myset4={'one','two','three','four','five','five'}


# In[14]:


myset4


# In[15]:


'six' in myset4


# In[16]:


'five' in myset4


# In[17]:


#methods
myset4.add('ten')


# In[18]:


myset4


# In[19]:


myset4.remove('one')


# In[20]:


myset4


# In[22]:


myset2.clear()


# In[23]:


myset2


# In[25]:


myset4.update([1,4,5,6,7])


# In[26]:


myset4


# In[27]:


#set operation
#union(return combination of two sets)
A={4,5,7,8}
B={7,9,0,4,8}
A.union(B)


# In[28]:


#intersection(return common element among sets)
A={3,45,7,8}
B={4,5,6,9,7}
A.intersection(B)


# In[29]:


#difference(specify difference elemnts in set)
A={3,4,5,6,7,8}
B={4,9,0,1,3}
A.difference(B)


# In[ ]:




