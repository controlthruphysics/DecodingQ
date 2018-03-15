#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string

class covfefe():

  def __init__(self):
    pass

  def displayletters(self):#Displays all lower case letters
    alphabet = string.ascii_lowercase[:]
    y = 1
    new = str()
    for ch in alphabet:
      if y < 9:
        new = new + ch + " "
      else:
        new = new + ch + "  "
      y += 1
    print('\n')
    print(new)
  
  def displaynums(self):#Displays numbers 1 thru 26
    nums = str()
    for x in range(1,27):
        nums = nums + str(x) + " "
    print(nums,"\n")
  
  def inputtext(self): #This inputs text, converts to lower case, removes spaces
    text = input("Enter text string:\n").lower().replace(" ","")
    return text
  
  def inputkey(self):
    key = input("\nEnter key:\n").lower()
    return key
  
  def modtext(self,text):
    result = str() 
    clean = str() 
    output = []
    for ch in text:
      result = result + ch + "  "
    print(result)
    for character in text:
      number = ord(character) - 96
      output.append(number)
    for ch in output:
      if ch > 9:
        clean = clean + str(ch) + " "
      else:
        clean = clean + str(ch) + "  "
    print(clean)
    return output 
  
  def buildkeydict(self,text,key):#Builds key dictionary from key input
    keyout = []
    clean = str()
    for char in key:
      num = ord(char) - 96
      keyout.append(num)
    newdict = []
    s = 0
    for r in range(len(text)):
      newdict.append(keyout[s])
      s += 1
      if s >= len(keyout):
        s = 0
    for r in range(len(newdict)):
      if newdict[r] > 9:
        clean = clean + str(newdict[r]) + " "
      else: 
        clean = clean + str(newdict[r]) + "  "
    print(clean)
    keyclean = str()
    s = 0
    for r in range(len(newdict)):
      keyclean = keyclean + key[s] + "  "
      s += 1
      if s >= len(key): s = 0
    print(keyclean)
    return newdict
  
  def getsum(self,output,newdict):
    z=0
    sumdict = []
    for x in range(len(output)):
      total = output[z] + newdict[z]
      if total > 26: total -= 26
      sumdict.append(total)
      z += 1
    cleansum = str()
    for x in sumdict:
      if x > 9:
        cleansum += str(x) + " "
      else:
        cleansum += str(x) + "  "
    print(cleansum)
    answer = []
    i = 0
    for x in range(len(sumdict)):
      answer.append(chr(sumdict[i]+96))
      i += 1
    cleananswer = str()
    i = 0
    for x in range(len(sumdict)):
      cleananswer += str(answer[i]) + "  "
      i += 1
    print(cleananswer)
    return cleananswer

  def getdictwords(self): #reads words from the dictionary file
    lines = [line.rstrip('\n').lower() for line in open('words')]
    return lines

  def findwords(self,text):
    words = self.getdictwords()
    print("Possible words:")
    for word in words:
      if word in text and len(word)>1:
        print(word)   

  def tryagain(self):
    again = input("\nEnter q to quit. Press any key to try again:\n")
    return again

if __name__ == "__main__":
  while True:
    cov = covfefe()
    text = cov.inputtext()
    key = cov.inputkey()
    cov.displayletters()
    cov.displaynums()
    output = cov.modtext(text)
    newdict = cov.buildkeydict(text,key)
    code = cov.getsum(output,newdict).replace(" ","")
    print('\n')
    cov.findwords(code)
    again = cov.tryagain()
    if again == "q": break
    else: continue
