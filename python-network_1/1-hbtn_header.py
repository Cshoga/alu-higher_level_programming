#!/usr/bin/python3
"""
Python script that recieves a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as reponse:
        html = reponse.info()
        print(html.get('X-Request-Id'))
