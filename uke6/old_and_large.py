import sys,os,shutil,time
move = True
usage = sys.argv[0]
try:
	path = sys.argv[1]
except:
	print "Bad usage of ",usage
	sys.exit()
new_home = path+'/send_to_Trash'
if not os.path.isdir(new_home):
	os.mkdir(new_home)
time = time.time()
day =60*60*24 
limit = 100 #number of days
limit_Mb = 1.0
Mb = float(1024*1024)
movedfiles = []

for (paths,dirs,files) in os.walk(path):
	for filename in files:
		elf = paths+'/'+filename
		size = os.path.getsize(elf)/Mb
		time1 = (time-os.path.getatime(elf))/day
		if time1>=limit and size>=limit_Mb:
			#print elf, time1, size
			#print new_home
			if move:
				shutil.copy(elf,new_home)
				os.remove(elf)
			movedfiles.append(filename)
if move and len(movedfiles)!=0:
	print "Done! The following %d files were moved: "%len(movedfiles)
	for i in movedfiles:
		print i
elif len(movedfiles)==0:
	print "No old or large files"
else:
	print "Done! The following files are older than %d days, and larger than %g Mb"%(limit,limit_MB)
'''
fredrik@fredrik-Aspire-V3-571:~/inf3331/uke6$ python old_and_large.py ~/inf3331/uke6/tmptree
Done! The following 5 files were moved: 
tmpf-19120
tmpf-165459
tmpf-544825
tmpf-93296
tmpf-188037
'''

