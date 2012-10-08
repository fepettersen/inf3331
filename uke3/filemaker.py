from math import sin,exp,cos,pi
from numpy import linspace
n = 2000;
dt = 1./n;
t = linspace(0,2*pi,n)

sinevalues = [sin(i) for i in t]
outfile = open('sample_sin.txt','w')
for n in range(len(t)):
	outfile.write('%.12f  %.12f \n' % (sinevalues[n],t[n]))
outfile.close()

expvalues = [exp(-i) for i in t]
outfile = open('sample_exp.txt','w')
for n in range(len(t)):
	outfile.write('%.12f  %.12f \n' % (expvalues[n],t[n]))
outfile.close()

cosvalues = [cos(i) for i in t]
outfile =open('sample_cos.txt','w')
for n in range(len(t)):
	outfile.write('%.12f  %.12f \n' % (cosvalues[n],t[n]))
outfile.close()
