import re

class boggle():

  def getscrambled(self):
    x = input("Enter word to be descrambled: \n").lower()
    return x

  def regexmagic(self,x):
    regex = "^(?:" + "|".join("{}()".format(c) for c in x) + "){{{}}}".format(len(x)) + "".join("\\{}".format(i+1) for i in range(len(x))) + "$"
    for line in open('words'):
      for match in re.finditer(regex,line):
        print(match.group())

  def tryagain(self):
    again = input("\nEnter q to quit. Press any key to try again\n")
    if again == "q":
      y = 1
    else: y = 0
    return y

if __name__ == "__main__":
  y = 0
  bog = boggle()
  while True:
    scram = bog.getscrambled()
    bog.regexmagic(scram)
    y = bog.tryagain()
    if y == 1: 
      break
    else: continue
