#!/bin/bash

HOSTNAMES[0]=   #enter the host names into this array
HOSTNAMES[1]=   #second part of array to show how to make it


#Example of how to iterate over all hosts and run commands on them.
for h in $HOSTNAMES
do
	ssh $h "command to run; second command to run; third..."
done

