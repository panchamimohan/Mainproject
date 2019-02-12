import os, sys, errno
import subprocess
import re
import itertools
import nltk
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
# Import our modules from /modules
sys.path.append("modules")
import questionClassifier
import sourceContentSelector
import coref
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def contains_negative(sent):
  return "no" in sent or "not" in sent or "n't" in sent

# Answers a question from the information in article.
# Ranks all the sentences and then returns the top choice.
def answer(question, article):
    question = question.strip().rstrip("?").lower()
    question_type = questionClassifier.process(question)
    question = nltk.tokenize.word_tokenize(question)
    relevant = sourceContentSelector.getScoredSentences(question, article)
    top = max(relevant, key = lambda s: s[1])
    if question_type == "BOOLEAN":
      if contains_negative(top): return "No"
      else: return "Yes"
    else: return top[0]

def ans(article_name,question_file):
  #article_name = sys.argv[1]
  questions = open(question_file).read().split("\n")
  if(questions[len(questions)-1]==""):
    questions.remove("")
  print(questions)
  article = coref.process(article_name)
  for question in questions:
    print("***********************A*************************")
    print answer(question, article)
    print("***********************A*************************")

 
