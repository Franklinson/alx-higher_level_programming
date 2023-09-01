#!/usr/bin/python3
"""takes in a letter and sends a POST request to ..."""

import requests
import sys


def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}

    try:
        response = requests.post(url, params=params)

        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user(letter)
