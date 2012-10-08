'''
This program takes in an interval on the form '[a:b]' or '[a:b,step]' and a function written in python notation and writes the funcion values to a file with the function as the filename. eg:
user@comuter$ python xygenerator '[0,6.28,0.1]' 'sin(x)'
makes the file sin(x).txt with the values sin(0), sin(0+0.1),...
'''
import sys; import re; from math import *
r = r'\[[+\-]?(\d+\.*\d*):[+\-]?(\d+\.*\d*),?\s*(\d*.*\d*)?\]';
g = re.search(r,sys.argv[1]).groups()
if len(g[-1]==0):
	g[-1] = 1 
y = [float(g[0])+float(g[2])*i for i in range(int((float(g[1])-float(g[0]))/float(g[2]))+1)]
func = lambda x: eval(sys.argv[2]); infile = open('%s.txt'%sys.argv[2],'w');
for x in y:
	infile.write(str(func(x)));infile.write('\n')
infile.close()


