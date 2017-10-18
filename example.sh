#!/bin/bash

HOSTNAMES[0]=   #enter the host names into this array
HOSTNAMES[1]=   #second part of array to show how to make it

if [$1]					#example of how an if statement works
	then
		echo $0 		#name of this bash script
		echo $1			#will print out the first arg from the command line
elif [$2]
	then
		echo $2 		#will print out the second arg from the command line
		echo $# 		#number of args passed
else
		echo $@ 		#all args
		echo $USER 		#user running script
		echo $$ 		#process id of the script
fi

#Example of how to iterate over all hosts and run commands on them.
for h in $HOSTNAMES
do
	ssh $h "command to run; second command to run; third..."
done

