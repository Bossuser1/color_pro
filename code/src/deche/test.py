#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 00:05:37 2017

@author: traoreb
"""

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
  print ('Hello there', sys.argv[1])
  # Command line args are in sys.argv[1], sys.argv[2] ..
  # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()