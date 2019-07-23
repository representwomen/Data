
# coding: utf-8

# In[130]:


#import requests
#import lxml.html as lh
import pandas as pd
from datetime import datetime
#from bs4 import BeautifulSoup
#import urllib.request as urllib


# In[131]:


currentYear = datetime.now().year
print (currentYear)

#####   UPDATE URL HERE    #########
url ='https://cawp.rutgers.edu/levels_of_office/women-mayors-us-cities-'+str(currentYear)

print(url)


# In[136]:


dfs = pd.read_html(url,header=0, match='Vivian Jones', encoding='utf-8')

#encoding  match='Vivian Jones'

print(len(dfs[0]))

for df in dfs:
    print(df)


# In[135]:


dfs[0]


# In[138]:


dfs[0].to_csv(str(currentYear)+"mayorsover30000.csv", sep=',', encoding='utf-8')


# In[143]:


readme = open("READ_ME","w+")
readme.write("You will need to find a few names with accents and hand-fix the weird characters that get substituted for the letters with accents. Additionally, the 'Rank' column is for the rank of the city in terms of population, that's why there are so many numbers missing. Otherwise you should be good to go!\n If you have additional questions email me at harbert.marilyn@gmail.com\n-Marilyn Harbert")
readme.close()
