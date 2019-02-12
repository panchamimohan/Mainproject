
import re
import nltk
import random
def transform_IT_IS(sentence):
  if ("It is" in sentence):
    question = sentence.replace("It is", "What is")
    return (question, True)
  return (sentence, False)

def add_questionmark(sentence):
  if (sentence[len(sentence) - 1] == '.'):
    sentence = sentence[:len(sentence) - 1]
  return sentence + "?"


def transform(sentence):

  sentence = add_questionmark(sentence)   # '.' -> '?'

  (question, success) = transform_IT_IS(sentence)
  if success: return (question, True)


  BEING = [ "IS", "ARE", "WAS", "WERE"]
  tokens = nltk.word_tokenize(sentence)
  posTag = nltk.pos_tag([tokens[0]])[0]

  add_why = 0

 
  if (len(tokens) > 1 and tokens[1].upper() in BEING):
    tokens = [tokens[1].capitalize(), tokens[0].lower()] + tokens[2:]

    if (add_why):
      tokens = ["Why", tokens[0].lower()] + tokens[1:]

    question = " ".join(tokens)
    if ("," in question):
      question = question.split(",")[0] + "?"

    return (question, True)

  if (len(tokens) > 2 and tokens[2].upper() in BEING):
    tokens = [tokens[2].capitalize(), tokens[0].lower(), tokens[1].lower()] + tokens[3:]
    #return (" ".join(tokens), True)

    if (add_why):
      tokens = ["Why", tokens[0].lower()] + tokens[1:]

    question = " ".join(tokens)
    if ("," in question):
      question = question.split(",")[0] + "?"
    return (question, True)

  if (tokens[0].upper() == "IT"):
    tokens = ["What"] + tokens[1:]
    #return (" ",join(tokens), True)
    question = " ".join(tokens)
    if ("," in question):
      question = question.split(",")[0] + "?"
    return (question, True)



  return (sentence, False)


def process(sentences):
  questions = [ ]
  for sentence in sentences:
    (question, success) = transform(sentence)
    if (success): questions.append( question )
  return questions
