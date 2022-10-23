#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests 
import bs4


# In[5]:


res = requests.get('http://quotes.toscrape.com')


# In[7]:


res.text


# In[8]:


soup = bs4.BeautifulSoup(res.text, 'lxml')


# In[9]:


soup.select('.author')


# In[10]:


authors = set()

for name in soup.select('.author'):
    authors. add(name.text)


# In[11]:


authors


# In[19]:


quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)


# In[20]:


quotes


# In[22]:


for item in soup.select('.tag-item'):
    print(item.text)


# In[23]:


url = ('http://quotes.toscrape.com/page/')


# In[26]:


authors = set()

for page in range (1,10):
    page_url = url + str(page)
    
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)


# In[27]:


authors


# This another way to do the same thing

# In[28]:


page_url = url + str('9999999999999')


# In[30]:


res = requests.get(page_url)
soup  = bs4.BeautifulSoup(res.text,'lxml')


# In[34]:


'No quotes found!' in res.text


# In[37]:


page_still_valid = True

Authors = set()
page = 1

while page_still_valid:
    
    page_url = url + str(page)
    
    res = requests.get(page_url)
    if 'No quotes found!' in res.text:
        break
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    for name in soup.select('.author'):
        Authors.add(name.text)
    page = page + 1
    
    
    


# In[38]:


Authors


# In[ ]:




