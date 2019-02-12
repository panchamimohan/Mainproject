import requests
from dragnet import extract_content, extract_content_and_comments
# fetch HTML

def getcontent(url):
    r = requests.get(url)

    # get main article without comments
    content = extract_content(r.content)

    return content
