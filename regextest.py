#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
from covfefe import covfefe
from goose import goose
import re

if __name__ == "__main__":
  cov = covfefe()
  duck = goose()
  text = duck.textinput()
  key = duck.keyentry()
  code = duck.parsetext(text,key).split()
  print("\nPossible matches: ")
  for x in code:
    regex = "^(?:" + "|".join("{}()".format(c) for c in x) + "){{{}}}".format(len(x)) + "".join("\\{}".format(i+1) for i in range(len(x))) + "$"
    for line in open('words'):
      for match in re.finditer(regex,line):
        print(match.group())
