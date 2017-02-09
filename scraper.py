import requests
from bs4 import BeautifulSoup
import datetime

# defining details for each tournament

# Should I import datetime and automatically add year, so there's no required input?

def australian_open(year):
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/australian_open/' + str(year)
	scrape(url)

def us_open(year):
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/us_open/' + str(year)
	scrape (url)

def wimbledon(year):
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/wimbledon/' + str(year)

def french_open(year):
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/wimbledon/' + str(year)

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