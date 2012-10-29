#!/usr/bin/env python
import sys, math, string
from numpy import *
usage = 'Usage: %s infile' % sys.argv[0]

try:
    infilename = sys.argv[1]
except:
    print usage; sys.exit(1)

# load file into a list of lines
f = open(infilename, 'r'); lines = f.readlines(); f.close()

# the second line contains the increment in t:
dt = float(lines[1])

# the third line contains the name of the time series:
ynames = lines[2].split()

# store y data in a dictionary of lists of floats:

y = {}           # declare empty dictionary
# -------This is edited----------
# load data from the rest of the lines:
yvalues = loadtxt(infilename,skiprows=3)	#loads the data from file to an array as float. Skips the 3 first rows
for name in ynames:				# Set 
    y[name] = yvalues[:,0]
f.close()

#--------This is not edited-----------
print 'y dictionary:\n', y

# write out 2-column files with t and y[name] for each name:
for name in y.keys():
    ofile = open(name+'.dat', 'w')
    for k in range(len(y[name])):
        ofile.write('%12g %12.5e\n' % (k*dt, y[name][k]))
    ofile.close()
'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke9$ python convert2_wNumPy.py mergefile_Sep11_2012.txt 
y dictionary:
{'sample_sin.txt': array([ 0.        ,  0.00314316,  0.00628629, ..., -0.00628629,
       -0.00314316, -0.        ]), 'sample_exp.txt': array([ 0.        ,  0.00314316,  0.00628629, ..., -0.00628629,
       -0.00314316, -0.        ]), 'sample_cos.txt': array([ 0.        ,  0.00314316,  0.00628629, ..., -0.00628629,
       -0.00314316, -0.        ])}
'''

