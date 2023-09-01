#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request"""
import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    try:
        # Send a POST request to the specified URL
        with urllib.request.urlopen(url, data=data) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')
            print(response_body)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <URL> <email>")
    else:
        url = sys.argv[1]
        email = sys.argv[2]
        send_post_request(url, email)
