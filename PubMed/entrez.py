# importing the requests library
import requests
from bs4 import BeautifulSoup
from django.utils.text import slugify
from SWE573_Project.models import ArticleModel


# api-endpoint
Search_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"


# sending get request and saving the response as response object
r = requests.get(url=Search_URL, params={'term': 'brain',
                                         # 'version': '2.0',
                                         'db': 'pubmed',
                                         })

# extracting data in json format
data = r.content

soup = BeautifulSoup(data, 'lxml')


# print(soup.title.string)

# print(soup.authors)

article_id = []

for a in soup.find_all('id'):
    article_id.append(a.string)

# print(article_id)


# api-endpoint
Summary_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

str1 = ','.join(article_id)

# sending get request and saving the response as response object
r = requests.get(url=Summary_URL, params={'id': str1,
                                          'retmode': 'xml',
                                          'db': 'pubmed',
                                          })

# extracting data in json format
data = r.content

soup = BeautifulSoup(data, 'lxml')

General_article = []

# print(soup.title.string)

# print(soup.find_all('documentsummary'))
# print(soup)
for article in soup.find_all('pubmedarticle'):
    General_article_authors = []
    for a in article.find_all('author'):
        General_article_authors.append(a.find('forename').string + ' ' + a.find('lastname').string)
        # print(a.find('name').string)
    #article.find('abstract').get_text()
    General_article.append({'id': article.find('pmid').string, 'title': soup.title.string,
                            'authors': ','.join(General_article_authors),
                            'abstract':article.find('abstract').get_text()})

#print(General_article)

