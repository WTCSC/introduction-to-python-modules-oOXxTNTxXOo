import re
def count_chars(text):  #Count the number of characters in a text
    f = len(text)       #Count the number of characters in a text
    return f

def count_words(text):  #Count the number of words in a text
    e = text.split()    #splits words from text
    d = len(e)          #Count the number of words in a text
    return d

def count_sentences(text):  #Count the number of sentences in a text
    y = re.split("!|\?|\.", text)    #splits text at typical sentence ender symbols
    del y[-1]               # deletes final blank so that split is accurate
    y = len(y)              #Count the number of sentences in a text
    return y
