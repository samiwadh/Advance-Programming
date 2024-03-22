
# coding: utf-8

# In[2]:

import numpy as np 
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([4,5,6,7,8,9])
sum=arr1+arr2
sum


# In[4]:

product=arr1*arr2
product


# In[5]:

divide=arr1/arr2
divide


# In[8]:

moduler = arr1 % arr2
moduler


# In[11]:

expo1 = arr1**2
print(expo1)

expo2 = arr2**2
print(expo2)


# In[14]:

expo1 = arr1*arr1
print(expo1)


# In[15]:

# binary indexing, fasing indexing ,


# In[17]:

arr3 = arr1.dot(arr2)
arr3


# In[25]:

new_arr1 = arr1.reshape(2,3)
new_arr1


# In[26]:

new_arr2 = arr2.reshape(3,2) #  we use dot product when the dimenion are different 
new_arr2


# In[29]:

new_arr3 =new_arr1.dot(new_arr2)
new_arr3


# In[30]:

arr1


# In[31]:

new_arr3.dot(arr1)


# In[32]:

new_arr3.min()


# In[34]:

new_arr3.max()


# In[37]:

new_arr3


# In[36]:

new_arr3.min(axis=0) #it give us whole min number row 


# In[38]:

new_arr3.max(axis=0) #it give us whole max number row 


# In[39]:

new_arr3.min(axis=1) #it give us whole column number row 


# In[40]:

new_arr3.max(axis=1) #it give us whole max number row 


# In[42]:

new_arr3.sum()


# In[43]:

new_arr3.sum(axis=0) # adding row 1 to row 2 


# In[44]:

new_arr3.sum(axis=1) # adding column 1 to column 2 


# In[47]:

new_arr3.std() #standerd davtion


# In[48]:

new_arr3.mean()


# In[49]:

new_arr3


# In[50]:

np.median(new_arr3) # very important 


# In[51]:

np.mean(new_arr3)


# In[52]:

np.exp(new_arr3)


# In[56]:

import numpy as np
np.sqrt(new_arr3)


# # Reshaping Numpy Arrays

# In[71]:

arr=np.array([2,3,5,6,7,8,18,12,35,81])
arr


# In[74]:

new_arr = arr.reshape([5,2])
new_arr


# In[75]:

new_arr.ndim


# # ravel function convert higher dimensioal to one dimensioal

# In[76]:

new_arr.transpose()


# In[80]:

new_arr.ravel()


# In[87]:

arr4 = np.array([[1,2,3,4],[5,6,7,8,9]])
arr4


# In[89]:

new_arr7 = np.arange(24).reshape(6,4)
new_arr7


# In[94]:

new_arr7[2:3,1:3]


# In[107]:

a=new_arr7[3:4,1:3]
a


# In[108]:

b=new_arr7[5:6,1:3]
b


# In[109]:

print(a)
print(b)


# In[ ]:



