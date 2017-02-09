import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.atpworldtour.com/en/scores/current'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find(attrs={'class': 'scores-results-content'})

print table.prettify()


