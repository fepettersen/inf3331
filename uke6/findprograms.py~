programs = {
  'gnuplot'  : 'plotting program',
  'gs'       : 'ghostscript, ps/pdf interpreter and previewer',
  'f2py'     : 'generator for Python interfaces to F77',
  'swig'     : 'generator for Python interfaces to C/C++',
  'convert'  : 'image conversion, part of the ImageMagick package',
  }

installed = findprograms(programs.keys())
for program in installed.keys():
    if installed[program]:
        print "You have %s (%s)" % (program, programs[program])
    else:
        print "*** Program %s was not found on the system" % (program,)

def checksize1(arg, dirname, files):
	for file in files:
	# construct the file’s complete path:
		filename = os.path.join(dirname, file)
		if os.path.isfile(filename):
			size = os.path.getsize(filename)
		if size > 1000000:
			print '%.2fMb %s' % (size/1000000.0,filename)
		root = os.environ[’HOME’]
		os.path.walk(root, checksize1, None)
# arg is a user-specified (optional) argument,
# here we specify None since arg has no use
# in the present example

