import wikisearch
import allwebcontent
import newask
from googlesearch import search 
import wikipedia
import drag

def check(j):
	if "en.wikipedia.org" in j:
		return 1
	elif "www.youtube.com" in j:
	        return 2
	else :
		return 0

def process(query):

	for url in search(query, tld="co.in", num=2, stop=1, pause=2):
		res = check(url)
		if res == 1:
			wikisearch.process(query)
			newask.process("search_results.txt")
			break
		elif res != 2:
			drag.process(url)
			newask.process("search_results.txt")

  

