#!/bin/bash
# sends a request to that URL

curl -s "$1" | wc -c
