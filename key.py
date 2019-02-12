import os, sys, errno
import subprocess
import re
import itertools
import nltk
from rake_nltk import Rake
from nltk.stem import PorterStemmer
import bs4
sys.path.append("modules")
import ques_content
import coref
sys.path.append("keyword-extraction")
import keyword_extraction_w_parser
#import demo
import newask
import answer
import news_hunt
r = Rake()
query = []
with open('data.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

try:
    data.decode('ascii')
    asciidata = data
except:
    udata=data.decode("utf-8")
    asciidata=udata.encode("ascii", "ignore")
f = open("asciidata.txt","w")
f.write(asciidata)
f.close()
article_content = coref.process("asciidata.txt")    
selected_content = ques_content.process(article_content)
for sentence in selected_content:
    r.extract_keywords_from_text(sentence)
    query = query + r.get_ranked_phrases()
query1 = " ".join(query)
#print("keywords\n")
print(query1)
#demo.process(query1)
news_hunt.process(query1)
newask.process("data.txt")

answer.ans("news_hunt.txt","ques.txt")




