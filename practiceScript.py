#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 22:43:53 2016

@author: batman
"""

import sys

infile = open(sys.argv[1])

for line in infile:
    print(line, end="")

print()
    
infile.close()