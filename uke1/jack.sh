#!/bin/bash

trap control_c SIGINT

control_c()
{
	echo " done"
	exit
}

while :
	do
	echo "All work and no play makes Jack a dull boy."
	sleep 1
done

#fredrik@fredrik-Aspire-V3-571:~/uio/inf3331/uke1$ ./jack.sh
#All work and no play makes Jack a dull boy.
#All work and no play makes Jack a dull boy.
#^C done

