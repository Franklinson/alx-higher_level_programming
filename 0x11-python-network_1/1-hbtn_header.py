#!/usr/bin/python3
"""  sends a request to the URL and displays the value of the X-Request-Id """

import urllib.request
import sys


def fetch_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(f"X-Request-Id: {x_request_id}")
            else:
                print("X-Request-Id not found in response headers.")
    except urllib.error.URLError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = sys.argv[1]
        fetch_x_request_id(url)
