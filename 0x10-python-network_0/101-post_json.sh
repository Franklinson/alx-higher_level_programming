#!/bin/bash
# Send the JSON POST request using curl and display the response body
curl -s -X POST -H "Content-Type: application/json" -d "$2" "$1"
