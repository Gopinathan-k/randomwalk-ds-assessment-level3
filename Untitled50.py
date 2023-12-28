#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt


# In[8]:


book=pd.read_csv("books.csv")
book_tag=pd.read_csv("book_tags.csv")
rating=pd.read_csv("ratings.csv")


# In[11]:


print(book)


# In[12]:


print(book_tag)


# In[13]:



print(rating)


# # Q1:How many books do not have an original title [books.csv]?

# In[9]:


print("books that do not have an original title in books.csv is: ",book["original_title"].isnull().sum())


# # Q2 How many unique books are present in the dataset ? Evaluate based on the 'book_id' after removing records containing null values for original_title column in [books.csv] and corresponding records in [book_tags.csv] and [ratings.csv]

# In[16]:


book_new=book.dropna(subset=['original_title'])
new_tag=book_tag[book_tag['goodreads_book_id'].isin(book_new["book_id"])]
new_rating=rating[rating['book_id'].isin(book_new["book_id"])]
val=book_new["book_id"].nunique()
print(val)


# # Q3 How many unique users are present in the dataset [ratings.csv] ?

# In[17]:


print("Total number of unique present in the rating.csv are: ",rating["user_id"].nunique())


# # Q4 How many unique tags are there in the dataset [book_tags.csv] ?

# In[18]:


print("Total number of unique tags present in the book_tags.csv are: ",book_tag["tag_id"].nunique())


# # Q5 Which tag_id is the most frequently used ie. mapped with the highest number of books [book_tags.csv] ? (In case of more than one tag, mention the tag id with the least numerical value)’.

# In[ ]:





# In[20]:


highly_used_tag = book_tag['tag_id'].value_counts().idxmax()
print("The answer is : ",highly_used_tag)


# # Q6 Which book (title) has the most number of counts of tags given by the user [book_tags.csv,books.csv] .

# In[45]:


most_tagged_book_id = book_tag.groupby('goodreads_book_id')['count'].sum().idxmax()
most_tagged_book_title = book.loc[book['book_id'] == most_tagged_book_id, 'title'].values[0]
print(f"Book with the most number of tag counts: {most_tagged_book_title}")


# # Q7 Plot a bar chart with top 20 unique tags in descending order of ‘user records’ (the number of users tagged the given tag_id with the goodreads_book_id) [book_tags.csv]
# 
# 

# In[33]:


top_tags = book_tag.groupby('tag_id')['count'].sum().sort_values(ascending=False).head(20)
plt.figure(figsize=(12, 6))
top_tags.plot(kind='bar', color='orange')
plt.title('Top 20 Tags by User Records')
plt.xlabel('Tag ID')
plt.ylabel('User Records')


# In[ ]:




