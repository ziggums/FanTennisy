import requests
from bs4 import BeautifulSoup

url = 'http://www.atpworldtour.com/en/scores/current/montpellier/375/draws'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find(attrs={'class': 'scores-draw-table'})

for row in table.findAll('tr'):
	print row.prettify()

'''
For Brandon:
So the above for statment returns everything I need, but not in the base form.
However, when I try to run the following:

for row in table.findAll('tr'):
	for cell in row.findAll('td'):
		print cell.text

It prints out the names, seeds, etc. but not the stuff within 'td' that is
<img class

This would be nice since it's the url for the flag of the player, and I could
use that for my eventual front end.

I suppose I could call those separately, but I'm not sure if there would be an
easy way to match them up.

Is there a way I can get that URL in line with everything else, to make it nice and neat?
'''





