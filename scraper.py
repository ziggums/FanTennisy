import urllib2
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.atpworldtour.com/en/scores/current'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody', attrs={'class': 'day-table'})

print table.prettify()


