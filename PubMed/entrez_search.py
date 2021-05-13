
# importing the requests library
import requests
from bs4 import BeautifulSoup


# api-endpoint
URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"


# defining a params dict for the parameters to be sent to the API
PARAMS = {'term':'brain',
#'version': '2.0',
'db': 'pubmed',
}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

# extracting data in json format
data = r.content

soup = BeautifulSoup(data, 'lxml')


#print(soup.title.string)

#print(soup.authors)

article_id = []

for a in soup.find_all('id'):
    article_id.append(a.string)
    
    
print(article_id)

#abstract entrezde yok hocaya sorulacak.







