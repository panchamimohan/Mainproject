import requests
from dragnet import extract_content, extract_content_and_comments

# fetch HTML
def process(url):

	r = requests.get(url)
	f= open("search_results.txt","w")

	content = extract_content(r.content)
	f.write(content)
	f.close()
	
