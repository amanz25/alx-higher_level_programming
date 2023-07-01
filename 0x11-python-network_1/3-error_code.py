#!/usr/bin/python3
""" sends a request to the URL and displays the body """

import urllib.request as request
import urllib.error as error
from sys import argv


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
