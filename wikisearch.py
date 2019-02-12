from googlesearch import search 
import wikipedia
def process(query):
	f= open("search_results.txt","w")
	try:
		search = wikipedia.search(query)
    		for p in search:
    			pp = wikipedia.page(p)
    			f.write(pp.content.encode('utf-8'))
	except wikipedia.exceptions.DisambiguationError as e:
   		print("Error: {0}".format(e))
	f.close() 
	
