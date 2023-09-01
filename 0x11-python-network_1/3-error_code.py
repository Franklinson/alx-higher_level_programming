#!/usr/bin/python3
"""script that takes in a URL, sends a request"""

import sys
from urllib import error, request


if __name__ == "__main__":

    try:
        url = sys.argv[1]
        with request.urlopen(url) as message:
            print(message.read().decode("UTF-8"))
    except error.HTTPError as errors:
        print("Error code:", errors.code)
