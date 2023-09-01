#!/usr/bin/python3
"""takes your GitHub credentials (username and password)"""
import requests
import sys


def get_github_id(username, password):
    """Gets the GitHub ID of the user with the given username and password."""
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"Basic {password}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Error getting GitHub ID: {response.status_code}")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    github_id = get_github_id(username, password)
    print(f"{github_id}")
