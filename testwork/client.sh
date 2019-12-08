#!/bin/bash

if [ -n "$1" ]
then
	url=$1'/api/cpu'
else
	url='http://127.0.0.1:8001/api/cpu'
fi

while(true)
do
	usage=`top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}'`
	http POST $url usage=$usage
	sleep 10
done
