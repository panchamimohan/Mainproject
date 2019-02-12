import os, sys, errno
import subprocess
import re
import itertools
import nltk
from nltk.stem import PorterStemmer
import bs4

pronouns = set(["he", "she", "it", "its", "it's", "him", "her", "his","they",
                "their","we", "our","i","you","your","my","mine","yours","ours"])

resolved_articles = {}

def process(path_to_article):
  original_path = path_to_article
  try:
    if path_to_article in resolved_articles:
      return resolved_articles[path_to_article]
    fh = open("NUL","w")
    subprocess.call(["./arkref.sh", "-input", path_to_article], stdout = fh, stderr = fh)
    fh.close()

    #tagged_article = open(path_to_article.replace("txt", "tagged")).read()
    tagged_article = "<root>"+tagged_article+"</root>" 
    soup = bs4.BeautifulSoup(tagged_article, "html.parser").root
    for entity in soup.find_all(True):
      if entity.string != None and entity.string.strip().lower() in pronouns:
        antecedent_id = entity["entityid"].split("_")[0]
        antecedent = soup.find(mentionid=antecedent_id)
        antecedent = str(antecedent).split(">", 1)[1].split("<", 1)[0]
        entity.string.replace_with(antecedent)
    resolved = re.sub("<.*?>", "", str(soup))
  except:
    resolved = open(original_path).read()

  resolved_articles[path_to_article] = resolved
  return resolved
