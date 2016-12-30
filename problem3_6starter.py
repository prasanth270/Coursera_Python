# -problem3_6.py *- coding: utf-8 -*-

import sys


infile = open(sys.argv[1])
outfile = open(sys.argv[2], 'w')

for line in infile:
    line = line.strip("\n")
    outfile.write(str(len(line)))
    outfile.write("\n")
    
infile.close()
outfile.close()