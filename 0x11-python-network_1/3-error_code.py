#!/usr/bin/python3
"""script that takes in a URL, sends a request"""

import sys
import urllib.request
import urllib.error


def fetch_url_content(url):
    try:
        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            content = response.read().decode('utf-8')
            return status_code, content
    except urllib.error.HTTPError as e:
        return e.code, None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    status_code, content = fetch_url_content(url)

    if content is not None:
        print(f"HTTP Status Code: {status_code}")
        print(content)
    else:
        print(f"Error code: {status_code}")
