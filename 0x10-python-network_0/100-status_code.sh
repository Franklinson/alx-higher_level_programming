#!/bin/bash
# Send the request using curl and store the response in a temporary file
curl -s -o response.txt -w "%{http_code}" "$1"
