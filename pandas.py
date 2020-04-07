#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[1]:


import pandas as pd


# In[24]:


groceries = pd.Series(index = ["Eggs","Milk","Bread","Apples"], data = [12,"No","Yes",5])
print(groceries)
print(groceries.shape)
print(groceries.size)
print(groceries.ndim)
print("The labels in groceries are: ",groceries.index)
print("Tha data in groceries is: ",groceries.values)
print("banana" in groceries)
print("Bread" in groceries)


# In[25]:


print(groceries[0],groceries["Eggs"])
print(groceries[[1,2]],groceries[["Milk","Bread"]])
print(groceries.iloc[[-1]])
print(groceries.loc[["Apples"]])
groceries["Eggs"] = 6
groceries.drop("Milk")
print(groceries)
groceries.drop("Milk",inplace=True)
print(groceries)


# In[11]:


items = {"Hasnain":pd.Series(data = [18,"Student","NED",3.97],index = ["Age","Designation","Institute","GPA"]),
         "Ahmed":pd.Series([18,"Iqra"],["Age","Institute"])}
info = pd.DataFrame(items)
info


# In[15]:


print(info.columns)
print(info.index)
print(info.values)
print(info.ndim)
print(info.shape)
print(info.size)


# In[17]:


hasnain_info = pd.DataFrame(items,columns = ["Hasnain"])
hasnain_info


# In[20]:


uni_info = pd.DataFrame(items, index = ["Institute"])
uni_info


# In[66]:


data = {"int":[10,50,100],"float":[0.0,1.0,2.0]}
info = pd.DataFrame(data,index=["label1","label2","label3"])
info
elements = [{"Bags":5,"Books":10},{"Bags":6,"Books":12}]
info2 = pd.DataFrame(elements,index = ["Store 1","Store 2"])
info2.loc[["Store 2"]]
info2[["Books"]]
#dataframe[column][row]
info2["Bags"]["Store 1"]
info2["Registers"] = [10,20]
info2
new = [{"Bags": 3,"Registers":12,"Books":14}]
info2 = info2.append(pd.DataFrame(new,index = ["Store 3"]))
info2["New Books"] = info2["Books"][1:]
#dataframe.insert(loc,label,data)
info2.insert(2,"Papers",[2,4,6])
info2.pop("New Books")
info2 = info2.drop(["Papers"],axis = 1)
info2 = info2.drop(["Store 2"],axis=0)
info2 = info2.rename(index = {"Store 3":"Store 2"})
info2


# In[82]:


items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]
store_items = pd.DataFrame(items2,index = ["Store 1","Store 2","Store 3"])
#Calculating Null Values
x = store_items.isnull().sum().sum()
x


# In[70]:


store_items


# In[72]:


store_items.dropna(axis = 0)


# In[73]:


store_items.dropna(axis = 1)


# In[83]:


store_items.fillna(0) #inplace = False


# In[84]:


store_items.fillna(method="ffill",axis=1) #0 for columns, Forward Filling


# In[86]:


store_items.fillna(method="backfill",axis=0) #Backward Filling


# In[88]:


store_items.interpolate(method="linear",axis=1)


# In[90]:


#Manipulate a DataFrame
import pandas as pd
import numpy as np

# Since we will be working with ratings, we will set the precision of our 
# dataframes to one decimal place.
pd.set_option('precision', 1)

# Create a Pandas DataFrame that contains the ratings some users have given to a
# series of books. The ratings given are in the range from 1 to 5, with 5 being
# the best score. The names of the books, the authors, and the ratings of each user
# are given below:

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame. 

# Create a dictionary with the data given above
dat = {"Author":authors,"Book Title":books,"User 1":user_1,"User 2":user_2,"User 3":user_3,"User 4":user_4}

# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)

# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:

book_ratings.fillna(book_ratings.mean(),inplace = True)
best_rated = book_ratings[(book_ratings == 5).any(axis = 1)]['Book Title'].values
best_rated


# In[ ]:


#pd.read_csv("FILENAME")
#DataFrame.head(n) for first n values
#DataFrame.tail(n) for last n values
#DataFrame.isnull().any()
#DataFrame.describe()
#DataFrame[Column_Name].describe()
#DataFrame.corr()
#DataFrame.groupby(["Year"])["Salary"].sum()

