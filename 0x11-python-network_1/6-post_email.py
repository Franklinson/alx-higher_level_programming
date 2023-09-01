#!/usr/bin/python3
"""Send a POST request to a specified URL with an email parameter."""

import requests
import sys


if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(res.text)
