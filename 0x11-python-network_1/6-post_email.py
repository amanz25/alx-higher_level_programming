#!/usr/bin/python3
""" sends a POST request to the passed URL """

import requests
from sys import argv


if __name__ == '__main__':
    req = {'email': argv[2]}
    r = requests.post(argv[1], data=req)
    print(r.text)
