"""
This program reads the filename to a textfile from the commandline and counts the number of occurances 
for each word in that file (book). The results are printed alphabetically to a report file called 
<inputfile>_report.txt.
"""

import sys

try:
	infilename = sys.argv[1]
except:
	print "Please provide a textfile on the commandline"
	sys.exit(1)

infile = open(infilename,'r')
lines = []

for line in infile:
	temp = line.split()	
	for word in temp:	#run through every word in the file
		nntemp = word.split('--')	#ran into trouble because words were separated by -- and no space
		if len(nntemp)>1:
			for i in nntemp:
				lines.append((i.strip(""".',_;"-:*!?&+()[]""")))	#strip all words of boundary symbols
		else:
			lines.append((word.strip(""".,_;"-:*'!?&+()[]""")))		#same

infile.close()
keywords = {}

for word in lines:
	if word not in keywords.keys():		# count occurances of every word except garbage
		if word != '' and word != "'":
			keywords[word] = 1
	else:
		keywords[word] += 1
		
infilename = infilename.split('.')[0]
reportname = infilename +'_report.txt'
outfile = open(reportname,'w')

for key, value in sorted(dict.items(keywords)):		#print to file alphabetically
	outfile.write(key),outfile.write('    '+str(value)+'\n')

outfile.close()
print 'Done! Report is stored in file %s' % reportname

'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke9$ python gutenberg.py blackwood.txt Done! Report is stored in file blackwood_report.txt
'''
