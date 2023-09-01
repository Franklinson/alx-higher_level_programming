#!/usr/bin/python3
"""Send a POST request to a specified URL with an email parameter."""

import requests
import sys


def send_post_request(url, email):
    response = requests.post(url, data={'email': email})
    return response.content


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response = send_post_request(url, email)

    if response.status_code == 200:
        print("POST request successful. Response content:")
        print(response.content.decode('utf-8'))
    else:
        print(f"POST request failed with status code {response.status_code}")
