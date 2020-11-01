#!/bin/bash

for file in `ls data`; do
	path="data/"
	if [ ${file: -11} == "_output.txt" ]
        then 
		python sequence_scoring.py $path$file
    	fi
done;


