#!/usr/bin/python3
# -*- coding: utf-8 -*-
#All that above this means run in python3 and use utf-8 characters
import string  # a python package I need to quickly grab all ascii letters
import re # python package regular expressions - tools for searching/parsing text

class goose(): #this defines a class

  def __init__(self): #runs upon class instatiation
    pass  #means do nothing, a place holder

  def textinput(self):  #this function lets you input text
    text = input('\nEnter text: \n') #outputs this string and waits for input
    return text #when the function is called, this is returned

  def keyentry(self): # lets you input the key, can be letter or number
    oldkey = input('\nEnter key, letter or number: \n').lower() # converts to lower case
    try: oldkey = int(oldkey)
    except: pass
    if isinstance(oldkey, str): # if you put in a string...
      key = ord(oldkey)-96  # convert to 1-26 number from ascii
    elif isinstance(oldkey,int): # if key entered is integer do this
      key = oldkey # just return the number you entered
    else: # in case something other than a integer or letter
      print("Invalid key")  # means you fucked up
      key = 0  # means no key for you
    print('Key is: ',key,'\n') 
    return key # return this key to calling function

  def displayletters(self):#Displays all lower case letters
    alphabet = string.ascii_lowercase[:] #needed import string for this
    y = 1 # variable I use for counting
    alpha = str() # declare empty string alpha
    for x in alphabet: # for each character in the alphabet
      if y < 9:   # for the first 9 letters give me 1 space
        alpha = alpha + x + " "
      else: # for the last letters give me 2 spaces, because of their numbers above/below
        alpha = alpha + x + "  "
      y += 1  # same as y = y + 1, same as add 1 to y
    print('\n') # the \ is an escape character. \n means new line
    print(alpha) # print out my newly spaced letters 

  def displaynums(self):#Displays numbers 1 thru 26
    nums = str() # make nums strings so can be concatenated
    for x in range(1,27): # do this 26 times (the 27 doesn't count)
        nums = nums + str(x) + " " # concatenate each string num with a space
    print(nums,"\n") # print result plus a new line

  def parsetext(self,text,key):
    y = 1  # the counting variable I use (iterator)
    parsed = [] # a list I'm declaring
    pretty = str() # new string I'm declaring
    for x in text: # for every letter,number,space,period,etc... in the text
      if y % key == 0: # if the remainder of y when divided by key is zero, BINGO
        parsed.append(x) # add it to the list
      y += 1 # increment the counter
    for x in parsed: # for every letter that made the list
      pretty = pretty + x # this concatenates the letters to make it pretty
    print('\n',pretty)
    return pretty # return parsed text to calling function

  def getdictwords(self): #reads words from the dictionary file
    lines = [line.rstrip('\n').lower() for line in open('words')]
    return lines

  def findwords(self,text): 
    words = self.getdictwords()
    print("\nPossible words:")
    for word in words:
      if word in text and len(word)>1:
        print(word)   

if __name__ == "__main__": # when running the computer starts here
  duck = goose() # duck is an instantiation of my class goose, means start using this class
  duck.displayletters() # call function to display letters
  duck.displaynums() # call function to display numbers
  mytext = duck.textinput() # call function to input text
  mykey = duck.keyentry() # call function to enter key
  code = duck.parsetext(mytext,mykey) # call function to parse text using key
  duck.findwords(code)
