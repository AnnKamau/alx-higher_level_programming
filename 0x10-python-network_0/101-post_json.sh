#!/bin/bash
"""sends a JSON POST request to a URL passed as the first argument"""

if [ -f "$2" ]
then
	curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
	if [ $? -eq 0 ]
	then
		echo "Valid JSON"
	else
		echo "Not Valid JSON"
	fi
else
	echo "File not found!"
fi

