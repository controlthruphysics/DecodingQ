#!/usr/bin/python3
# -*- coding: utf-8 -*-
import string
from covfefe import covfefe
from goose import goose
if __name__ == "__main__":
  cov = covfefe()
  duck = goose()
  text = duck.textinput()
  key = duck.keyentry()
  code = duck.parsetext(text,key)
  
