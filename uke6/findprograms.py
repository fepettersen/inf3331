"""
This program is supposed to check wether or not the programs in the dictionary programs exists in the current directory
"""
import os.path
programs = {  'gnuplot'  : 'plotting program',
  'gs'       : 'ghostscript, ps/pdf interpreter and previewer',
  'f2py'     : 'generator for Python interfaces to F77',
  'swig'     : 'generator for Python interfaces to C/C++',
  'convert'  : 'image conversion, part of the ImageMagick package'}
def findprograms(program):
    f = {};
    for i in program:
        f[i]=os.path.basename(i)
    return f

installed = findprograms(programs.keys())

for program in installed.keys():
    if installed[program]:
        print "You have %s (%s)" % (program, programs[program])
    else:
        print "*** Program %s was not found on the system" % (program,)
'''
fredrik@fredrik-Aspire-V3-571:~/Dropbox/uio/inf3331/uke6$ python findprograms.py 
You have convert (image conversion, part of the ImageMagick package)
You have gs (ghostscript, ps/pdf interpreter and previewer)
You have swig (generator for Python interfaces to C/C++)
You have gnuplot (plotting program)
You have f2py (generator for Python interfaces to F77)
'''
