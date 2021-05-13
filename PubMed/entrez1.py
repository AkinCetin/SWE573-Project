import requests
from bs4 import BeautifulSoup

# api-endpoint
Search_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# sending get request and saving the response as response object
r = requests.get(url=Search_URL, params={'id': '16776593',
                                         # 'version': '2.0',
                                         'db': 'pubmed',
                                         'api_key': '3063d8b2cf50fafdb90195ee618a9e80e909',
                                         })

# extracting data in json format
data = r.content

soup = BeautifulSoup(data, 'lxml')


#print(soup.find('Pubmed-entry'))

print(soup)