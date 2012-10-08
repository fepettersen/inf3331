#!/usr/bin/env python

import time, sys
from os import rename
try:
	filename = sys.argv[1]
except:
	print 'Please provide a filename os the commandline'
	sys.exit()

date = time.asctime() #acuire date
date = date.split()
space = '_'; dot = '.'
new_date = space+date[1]+date[2]+space+date[-1] #create a string with the date on the wanted form
temp = filename.split('.')
new_filename = temp[0]+new_date+dot+temp[1] # create the new filename
print new_filename

rename(filename,new_filename) # Rename the file
'''
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke3$ python add_date.py mergefile.txt 
mergefile_Sep11_2012.txt
'''
