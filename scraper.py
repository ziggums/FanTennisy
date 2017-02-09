import requests
from bs4 import BeautifulSoup

url = 'http://www.atpworldtour.com/en/scores/current/montpellier/375/draws'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find(attrs={'class': 'scores-draw-table'})

for row in table.findAll('tbody'):
	for cell in row.findAll('tr'):
		print cell.text # text in cell
		print cell.find('img') # image in cell





