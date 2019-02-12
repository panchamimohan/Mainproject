
import re
import nltk


def entity_score(sentence):
  tokens = nltk.word_tokenize(sentence)
  tokensU = map(lambda (x): x.upper, tokens)
  if (2 < len(tokens) and len(tokens) < 12):
    if ("IS" in tokensU or "WAS" in tokensU or
        "WERE" in tokensU or "BEING" in tokensU or
        "ARE" in tokensU):
      if (nltk.pos_tag([tokens[0]])[0] == "PRP"):
        return 1.0
      else:
        return 0.5
  score = 0
  return score

def naive_score(sentence):
  word_count = len(nltk.word_tokenize(sentence))
  weird = not any((c in sentence) for c in "?;:[]()"),

  features = [
    not weird,             
    "It is" in sentence,   
    " is " in sentence,    
    4 < word_count < 12,
    5 < word_count < 7
  ]
  return float(sum(features))/len(features)

def sentence_score(sentence):
  return 0.1*naive_score(sentence) + 0.9*entity_score(sentence)

def process(source_text):
  sentences = nltk.sent_tokenize(source_text)
  sentences = sorted(sentences, key = lambda (x): -sentence_score(x))
  return sentences
