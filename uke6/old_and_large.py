import sys,os,glob,time

usage = sys.argv[0]
try:
	path = sys.argv[1]
except:
	print "Invalid usage in ",usage
	sys.exit()
time = time.atime()
for elf in os.path.glob(path):
	if os.path.getatime(elf)
