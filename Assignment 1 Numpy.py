#!/usr/bin/env python
# coding: utf-8

# # 1. Create a null vector of size 10 but the fifth value which is 1.

# In[6]:


import numpy as np


arr = np.zeros(10,dtype = int)
arr[4] = 1

print(arr)


# # 2. Create a vector with values ranging from 10 to 49.

# In[8]:


arr_1 = np.arange(10,50)

arr_1


# # 3. Create a 3x3 matrix with values ranging from 0 to 8

# In[9]:


arr_2 = np.arange(0,9).reshape(3,3)

print(arr_2)


# #  4. Find indices of non-zero elements from [1,2,0,0,4,0]

# In[16]:


non_zero = np.nonzero([1,2,0,0,4,0])
print(non_zero)


# # 5. Create a 10x10 array with random values and find the minimum and maximum values.
# 

# In[12]:


import numpy as np
n_arr = np.random.random((10,10))

print("the original array",n_arr)

print("\n\n")
print("the minimum value of n_arr: \n",n_arr.min())
      
print("\n\n")
print("the maximun value of n_arr: \n",n_arr.max())


# # 6. Create a random vector of size 30 and find the mean value.

# In[14]:


import numpy as np

a = np.random.random(30)
print("the random array is: \n",a)

mean_1 = a.mean()
print("\n\nthe mean value of array: \n ",mean_1)


# In[ ]:




