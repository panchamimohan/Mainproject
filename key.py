import os, sys, errno
import subprocess
import re
import itertools
import nltk
import bs4
from rake_nltk import Rake
sys.path.append("modules")
import ques_content
import coref
sys.path.append("keyword-extraction")
#import demo
import newask
import answer
import news_hunt
sys.path.append("question-generation")
import question
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
#newask.process("data.txt")
v = question.makequestion(data)
print(v)
qu = open("ques.txt","w")
print(qu)
for x in v:
    y = x['Q']
    qu.write(y)
    print(x['Q'])
qu.close()
answer.ans("news_hunt.txt","ques.txt")
