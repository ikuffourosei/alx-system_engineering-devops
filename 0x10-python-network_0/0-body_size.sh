#!/bin/bash
# a Bash script that takes in a URL and displays the size of the body of the response
if [ $# -lt 1 ]; then
    echo "Usage: $0 [URL]"
else
    SIZE=$(curl -sI "$1" | grep -i Content-Length | awk {print $2})
    echo $SIZE
fi 
