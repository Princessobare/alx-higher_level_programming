#!/usr/bin/python3
"""This script:
- takes a URL,
- sends request to the URL and displays the value
- of X-Request-Id variable in the response header.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    requests = urllib.request.Request(url)
    with urllib.request.urlopen(requests) as response:
        print(dict(response.headers).get("X-Request-Id"))
