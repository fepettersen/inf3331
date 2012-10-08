'''
A program which sorts output from a system test after decreasing CPU-time
'''
import sys

try:
	filename = sys.argv[1]
except:
	print 'Please provide the filename of a suitable file on the \n commandline.'
	sys.exit()

	
timelist = []; indexlist = []
infile = open(filename)
i = 0
for line in infile:
	#extract all lines whith CPU-time
	if line.startswith('CPU-time:'):
		timelist.append(line)
	i+=1
N = len(timelist)
infile.close()
somelist = [0]*N
sortinglist = [0]*N

for i in range(N):
	#extract the actual CPU-time
	somelist[i] = timelist[i].split()
	sortinglist[i] = float(somelist[i][1])

n = 0
indexlist = [0]*N

while sum(sortinglist)>0:
	#extract the highest CPU-time value and store the index of
	#this element. Replace the highestCPU-time value by 0 for each 		#round.
	m = 0;index = 0
	for k in range(N):
		x = sortinglist[k]
		if x>m:
			m=x
			index = k
	sortinglist[index] = 0
	indexlist[n] = index	
	n+=1

finallist = [0]*N

for s in range(N):
	#Store the outputlines from test in a new list with decreasing
	#CPU-time
	finallist[s] = timelist[indexlist[s]]
	print '%s'% finallist[s]
'''
Runtime example:
fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke3$ python ranking.py efficiency.test 
CPU-time: 272.90   g77 -O0 formatted I/O
CPU-time: 255.97   f95 -O0 formatted I/O
CPU-time: 252.51   f95 -O3 formatted I/O
CPU-time: 252.47   f95 -O1 formatted I/O
CPU-time: 252.40   f95 -O2 formatted I/O
CPU-time: 243.93   f95 -O3 -Kloop -KPENTIUM_PRO -x - formatted I/O
CPU-time: 238.32   g77 -O2 formatted I/O
CPU-time: 236.01   g77 -O3 -ffast-math -funroll-loops formatted I/O
CPU-time: 234.90   g77 -O3 formatted I/O
CPU-time: 229.95   g77 -O1 formatted I/O
CPU-time:  56.54   g77 -O0 lambda array replaced by h(x,y) calls
CPU-time:  49.10   g77 -O0 lambda array replaced by h(0,0) calls
CPU-time:  45.37   g77 -O0 if-test inside the main loop
CPU-time:  43.50   g77 -O0 traversing the array rowwise
CPU-time:  42.94   g77 -O0 original (optimal?) code
CPU-time:  42.88   g77 -O2 lambda array replaced by h(x,y) calls
CPU-time:  42.78   g77 -O3 lambda array replaced by h(x,y) calls
CPU-time:  41.97   g77 -O3 -ffast-math -funroll-loops lambda array replaced by h(x,y) calls
CPU-time:  41.33   g77 -O1 lambda array replaced by h(x,y) calls
CPU-time:  37.91   g77 -O2 lambda array replaced by h(0,0) calls
CPU-time:  37.85   g77 -O3 lambda array replaced by h(0,0) calls
CPU-time:  37.59   g77 -O3 -ffast-math -funroll-loops lambda array replaced by h(0,0) calls
CPU-time:  37.56   g77 -O1 lambda array replaced by h(0,0) calls
CPU-time:  32.39   f95 -O0 lambda array replaced by h(x,y) calls
CPU-time:  30.55   f95 -O0 lambda array replaced by h(0,0) calls
CPU-time:  29.58   f95 -O3 -Kloop -KPENTIUM_PRO -x - if-test inside the main loop
CPU-time:  22.18   f95 -O3 -Kloop -KPENTIUM_PRO -x - lambda array replaced by h(0,0) calls
CPU-time:  19.58   f95 -O3 -Kloop -KPENTIUM_PRO -x - traversing the array rowwise
CPU-time:  19.45   f95 -O3 -Kloop -KPENTIUM_PRO -x - original (optimal?) code
CPU-time:  17.64   f95 -O3 -Kloop -KPENTIUM_PRO -x - lambda array replaced by h(x,y) calls
CPU-time:  15.97   f95 -O0 traversing the array rowwise
CPU-time:  15.84   f95 -O0 if-test inside the main loop
CPU-time:  15.27   f95 -O0 original (optimal?) code
CPU-time:  12.33   f95 -O1 lambda array replaced by h(0,0) calls
CPU-time:  12.33   f95 -O2 lambda array replaced by h(0,0) calls
CPU-time:  12.32   f95 -O3 lambda array replaced by h(0,0) calls
CPU-time:  12.32   f95 -O3 lambda array replaced by h(x,y) calls
CPU-time:  12.31   f95 -O1 lambda array replaced by h(x,y) calls
CPU-time:  12.30   f95 -O2 lambda array replaced by h(x,y) calls
CPU-time:  11.66   g77 -O1 if-test inside the main loop
CPU-time:   9.92   g77 -O2 if-test inside the main loop
CPU-time:   9.87   g77 -O3 if-test inside the main loop
CPU-time:   9.67   g77 -O3 -ffast-math -funroll-loops if-test inside the main loop
CPU-time:   9.52   f95 -O2 if-test inside the main loop
CPU-time:   9.47   f95 -O1 if-test inside the main loop
CPU-time:   9.45   f95 -O3 if-test inside the main loop
CPU-time:   8.26   g77 -O1 traversing the array rowwise
CPU-time:   7.67   g77 -O1 original (optimal?) code
CPU-time:   7.37   g77 -O2 traversing the array rowwise
CPU-time:   7.31   f95 -O3 traversing the array rowwise
CPU-time:   7.30   g77 -O3 traversing the array rowwise
CPU-time:   7.27   f95 -O1 traversing the array rowwise
CPU-time:   7.27   f95 -O2 traversing the array rowwise
CPU-time:   7.22   g77 -O3 -ffast-math -funroll-loops traversing the array rowwise
CPU-time:   6.04   f95 -O1 original (optimal?) code
CPU-time:   6.02   f95 -O2 original (optimal?) code
CPU-time:   6.02   f95 -O3 original (optimal?) code
CPU-time:   5.62   g77 -O2 original (optimal?) code
CPU-time:   5.55   g77 -O3 original (optimal?) code
CPU-time:   5.41   g77 -O3 -ffast-math -funroll-loops original (optimal?) code
'''
