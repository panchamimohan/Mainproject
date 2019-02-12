import json
import urllib2

import lxml
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup

def cleanme(html):
    soup = BeautifulSoup(html) # create a new bs4 object from the html data loaded
    for script in soup(["script"]): 
        script.extract()
    text = soup.get_text()
    return text

def process(quer):
	f= open("news_hunt.txt","w")
	data = {'query': quer}
	req = urllib2.Request('https://api-news.dailyhunt.in/api/v2/search/query')
	req.add_header('Content-Type', 'application/json')

	response = urllib2.urlopen(req, json.dumps(data))
	js = json.loads(response.read())
	data=js['data']
	count=data["count"]
	
	cleaner = Cleaner()
	cleaner.javascript = True # This is True because we want to activate the javascript filter
	cleaner.style = True 
	for i in range (count):
		row=data["rows"][i]["content"]
		cleanrow = cleanme(row)
		#cleanrow = cleanhtml(row)
		f.write(cleanrow)
	#print("***********************************************************************")
	#print(row)
	#print("***********************************************************************")
	

     # This is True because we want to activate the styles & stylesheet filter



