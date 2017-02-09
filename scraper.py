import requests
from bs4 import BeautifulSoup
import datetime

# defining details for each tournament

# Should I import datetime and automatically add year, so there's no required input?
# Also, how much of this should I put in the functions, and how much of it should 
def australian_open(year):
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/australian_open/' + str(year)
	scrape(url)

# function for calling data
def scrape(url):
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find(attrs={'class': 'dtable'})

	for row in table.findAll('tr'):
		for cell in row.findAll('td'):
			print (cell.text)

# Main Body Logic #
now = datetime.datetime.now()
year = now.year

australian_open(year)

