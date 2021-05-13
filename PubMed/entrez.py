# importing the requests library
import requests
from bs4 import BeautifulSoup


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
Summary_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

str1 = ','.join(article_id)

# sending get request and saving the response as response object
r = requests.get(url=Summary_URL, params={'id': str1,
                                          'version': '2.0',
                                          'db': 'pubmed',
                                          })

# extracting data in json format
data = r.content

soup = BeautifulSoup(data, 'lxml')

General_article = []

# print(soup.title.string)

# print(soup.find_all('documentsummary'))
# print(soup)
for article in soup.find_all('documentsummary'):
    General_article_authors = []
    for a in article.find_all('author'):
        General_article_authors.append(a.find('name').string)
        # print(a.find('name').string)
    General_article.append({'id': article.get('uid'), 'title': soup.title.string,
                            'authors': ','.join(General_article_authors)})

print(General_article)


# abstract entrezde yok hocaya sorulacak.
