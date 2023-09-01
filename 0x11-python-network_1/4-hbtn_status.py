#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import requests


def fetch_status():
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == "__main__":
    fetch_status()
