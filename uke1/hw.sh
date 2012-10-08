#!/bin/bash
r=$1 # store first command-line argument in r
s=`echo "$r" | bc -l`
# print to the screen:
echo "Hello, World! $r=$s"

#user@computer:~/uio/inf3331/uke1$ ./hw.sh 1+112
#Hello, World! 1+112=113


