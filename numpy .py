#!/usr/bin/env python
# coding: utf-8

# # Numpy

# In[3]:


from time import time
import numpy as np


# In[4]:


x = np.random.random(100000000)


# In[5]:


start = time()
sum(x) / len(x)
print(time() - start)


# In[2]:


start = time()
np.mean(x)
print(time() - start)


# ## Arrays

# In[27]:


a = np.array([1,2,3])
b = np.array([1.8,2,3.7], dtype = np.int64)
c = np.array([2,4,'6'], dtype = np.str)
d = np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[30]:


print("Array {}\nType {}\nElements Type: {}".format(d,type(d),d.dtype))
print("Dimensions: {}\nLength: {}".format(d.shape,d.size))


# In[33]:


np.save("array1",a)
print(np.load("array1.npy"))


# In[37]:


x = np.zeros((3,3),dtype=int)
print(x)


# In[40]:


x = np.ones((3),dtype=str)
print(x)


# In[42]:


x = np.full((4,3),5)
print(x)


# In[43]:


x = np.eye(5)
print(x)


# In[46]:


x = np.diag([1,2,3,4])
print(x)


# In[49]:


x = np.arange(0,30,2)
print(x)


# In[58]:


x = np.linspace(0,30,16)
print(x)


# In[60]:


x = np.reshape(x,(8,2))
print(x)


# In[65]:


y = np.arange(1,10).reshape((3,3))
print(y)


# In[67]:


x = np.random.random((4,5))
print(x)


# In[81]:


x = np.random.randint(1,11,(5))
print(x)
print(x.max())
print(x.min())
print(x.sum())


# In[82]:


x = np.random.normal(10,5,size=(3,3))
print(x)
print(x.mean())


# In[10]:


x = np.array([[1,2],[3,4]])
print(x[0,0])


# In[20]:


X = np.array([[1,2,3],[4,5,6],[7,8,9]])
X[1,1] = "20"
print(X)


# In[25]:


x = np.arange(1,10).reshape(3,3)
print(x)
x[0,1] = 0
x[0,2] = 0
x[1,0] = 0
x[1,2] = 0
x[2,0] = 0
x[2,1] = 0
print(x)


# In[36]:


x = np.arange(1,10).reshape(3,3)
y = np.delete(x,[0,1],axis=1)
print(x)
print(y)


# In[55]:


x = [1,2,3]
x = np.append(x,4)
print(x)
x = np.linspace(1,9,9).reshape(3,3)
print(x)
y = np.append(x,[[10,11,12]],axis=0)
print(y)
z = np.append(x,[[10],[11],[12]],axis=1)
print(z)


# In[57]:


y = np.insert(x,2,[2.5])
print(y)
z = np.insert(x,3,[10,11,12],axis=0)
print(z)


# In[63]:


x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.vstack((x,y))
w = np.hstack((x,y))
print(z,w)


# In[3]:


a = np.arange(1,17).reshape(4,4)
print(a)
print(a[1:,2:])
b = a.copy()
b = np.copy(a[2:,2:])
print(b)


# In[4]:


print(np.diag(b))
print(np.diag(a,k=1))
s = np.diag([1,2,1])
print(np.unique(s))


# In[19]:


X = np.arange(12).reshape(3,4)
print(X[(X>5) & (X<10)])
print(X[(X > 10) & (X < 17)])


# In[21]:


# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))


# In[2]:


x = np.random.randint(1,11,size=(10,))
print(x)
y = np.sort(x)
print(x)
x.sort()
print(x)
print(y)
print(np.sort(np.unique(x)))
a = np.random.randint(0,9,size=(4,3))
print(np.sort(a,axis=0))
print(np.sort(a,axis=1))


# In[5]:


a = np.array([1,2,3,4,5])
b = np.array([2,1,2,1,2])
print(np.add(a,b),a+b)
print(np.subtract(a,b),a-b)
print(np.multiply(a,b),a*b)
print(np.divide(a,b),a/b)
print(np.sqrt(a))
print(np.exp(a))
print(np.power(a,2))
print(a.sum())
print(a.mean())
print(a.std()) #axis = 0
print(a.max())
print(a.shape)
print(a.size)

