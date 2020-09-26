#9/26/2020
"""Problem Statement:
Given a string of words delimited by spaces, reverse the words in string. 
For example, given 'hello world here', return 'here world hello' """

def reverseStringOfWords(words):
    listOfWords = words.split() #delimit string 'words' using split() function, which uses space as default delimiter

    #Could have replaced the following 3 lines with reverse() function.
    listOfWordsReversed = []
    for i in listOfWords:
        listOfWordsReversed.insert(0,i + ' ') #insert each word + a space at the beginning of list
    
    wordsReversed = "".join(listOfWordsReversed)[:-1] #join() function to convert list to string, and [:-1] to
                                                      #remove the last space created from earlier for loop

    return wordsReversed 

words = "hello world here is a string of words"
wordsReversed = reverseStringOfWords(words)
print(wordsReversed) #prints 'words of string a is here world hello'
#Note: Could have also used reverse() function instead of for loop and insert() function.