#6/17/20
"""
Problem Statement:
Implement an autocomplete system. That is, given a query string s and a set of
all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string "de" and the set of strings
[dog, deer, deal], return [deer, deal].
"""

def autocomplete(s,allWords):
    suggestions = [word for word in allWords if word.startswith(s)]
    return s, allWords, suggestions

#Verification:
s, allWords, suggestions = autocomplete("de",["dog","deer","deal"])

#Implementing on a larger scale:
with open('2020-06-17_10000words.txt', 'r') as reader: #Open text file of 10,000 words.
    allWordsDict = reader.read().splitlines()
s2, allWords2, suggestions2 = autocomplete("mot",allWordsDict)
print(suggestions2) #Prints ['motel', 'motels', 'mother', 'motherboard', 'mothers',
                    #'motion', 'motivated', 'motivation', 'motor', 'motorcycle', 
                    #'motorcycles', 'motorola', 'motors'] from a list of 10,000 words.