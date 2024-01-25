#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request and get the body size in bytes
body_size=$(curl -sI "$1" | grep -i "content-length" | awk '{print $2}' | tr -d '\r\n')

# Display the body size in bytes
echo "$body_size"

