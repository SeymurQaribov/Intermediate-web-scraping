#!/usr/bin/env python
# coding: utf-8

# In[21]:


import bs4


import requests


# In[22]:


base_url = ('http://books.toscrape.com/catalogue/page-{}.html')


# In[23]:


ress = requests.get(base_url.format(1))


# In[24]:


soup1 = bs4.BeautifulSoup(ress.text, 'lxml')


# In[25]:


value= soup1.select('.product_pod')


# In[26]:


example = value[0]


# In[27]:


example.select('.star-rating.Three')


# In[28]:


example.select('a')[1]['title']


# In[29]:


two_star_title = []

for n in range(1,51):
    scarpe_url = base_url.format(n)
    ress = requests.get(scarpe_url)
    
    soup1 = bs4.BeautifulSoup(ress.text, 'lxml')
    books = soup1.select(".product_pod")
    
    for book in books:
        
        #if 'star_rating.Two' in str(book)-This is another different way to get two star ratnig book
        if len(book.select('.star-rating.Two'))!= [0]:
            book_title = book.select('a')[1]['title']
            two_star_title.append(book_title)
         
    


# In[30]:


two_star_title


# In[ ]:




