import os, sys, errno
import subprocess
import re
import itertools
import nltk
from nltk.stem import PorterStemmer
import bs4

sys.path.append("modules")
import questionContentSelector
import questionFromSentence
import coref
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def process(path_to_article):
  num_questions = 5
  f= open("ques.txt","w")

  article_content = coref.process(path_to_article)
  print("*****************article content*********************** \n")
  print(article_content)
  selected_content = questionContentSelector.process(article_content)
  print(selected_content)
  questions = questionFromSentence.process(selected_content)
  print(questions)
  questions = questions[:num_questions]
  for question in questions:
    f.write(question+"\n")
  f.close()
  
