require 'HTTParty'
require 'Nokogiri'
require 'JSON'
require 'Pry'
require 'csv'

def australian_open(year)
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/australian_open/' + year.to_s
end

def us_open(year)
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/us_open/' + year.to_s
end

def wimbledon(year)
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/wimbledon/' + year.to_s
end

def french_open(year)
	url = 'http://www.xscores.com/tennis/tournamentresults/atp-s/french_open/' + year.to_s
end

def scrape(url)
end

page = HTTParty.get('http://www.xscores.com/tennis/tournamentresults/atp-s/australian_open/2017')

Pry.start(binding)