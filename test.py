#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
from covfefe import covfefe

if __name__ == "__main__":
  cov = covfefe()
  text = cov.inputtext()
  words = cov.getdictwords()
  for word in words:
    if word in text and len(word) > 1:
      print(word)
