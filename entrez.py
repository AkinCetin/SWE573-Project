# importing the requests library
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from django.utils import timezone
from datetime import datetime
from SWE573_Project.models import ArticleModel
from django.utils.text import slugify
from bs4 import BeautifulSoup
import requests





# api-endpoint
Search_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

TERMS = ['lung', 'brain']
for term in TERMS:
        

    # sending get request and saving the response as response object
    r = requests.get(url=Search_URL, params={'term': term,
                                            # 'version': '2.0',
                                            'db': 'pubmed',
                                            'retmax': '400'
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

    for i in range(0,len(article_id), 200):





        str1 = ','.join(article_id[i:i+200])

        # sending get request and saving the response as response object
        r = requests.get(url=Summary_URL, params={'id': str1,
                                                'retmode': 'xml',
                                                'db': 'pubmed',
                                                })

        # extracting data in json format
        data = r.content

        soup = BeautifulSoup(data, 'lxml')

        General_article = []
        General_article_keywords = []

        # print(soup.title.string)

        # print(soup.find_all('documentsummary'))
        # print(soup)
        for article in soup.find_all('pubmedarticle'):
            General_article_authors = []
            for a in article.find_all('author'):
                first_name = a.find('forename')
                last_name = a.find('lastname')
                if not first_name:
                    first_name = ''
                else:
                    first_name = first_name.string
                if not last_name:
                    last_name = ''
                else:
                    last_name = last_name.string

                General_article_authors.append(
                    first_name + ' ' + last_name)
                    
                for b in article.find_all('keywordlist'):
                    keyword = b.find('keyword')
                    if not keyword:
                        keyword = ''
                    else:
                        keyword = keyword.string

                    General_article_keywords.append(keyword)
                

                # print(a.find('name').string)
            # article.find('abstract').get_text()
            article_date = article.find('articledate')
            if article_date:
                article_date = datetime.strptime(article_date.find('year').string + '-' + article_date.find(
                    'month').string + '-' + article_date.find('day').string, '%Y-%m-%d')
            General_article.append({'id': article.find('pmid').string, 'title': article.find('title').string,
                                    'authors': ','.join(General_article_authors),
                                    'abstract': article.find('abstract').get_text() if article.find('abstract') else '',
                                    'keywords': ','.join(General_article_keywords),
                                    'publish_date': article_date},)

        # print(General_article)

        for a in General_article:
            ArticleModel.objects.update_or_create(pmid=a.get('id'), defaults={
                'title':a.get('title'), 'body':a.get('abstract'), 'authors':a.get(
                'authors'), 'pmid': a.get('id'), 'publish_date':a.get('publish_date'), 'slug':slugify(a.get('title'))
            })
