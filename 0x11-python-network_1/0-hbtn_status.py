#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

from urllib.request import Request, urlopen
from urllib.error import URLError

if __name__ == "__main__":
    try:
        rq = Request('https://alx-intranet.hbtn.io/status')
        with urlopen(rq) as r:
            res = r.read()
            print("Body response:")
            print("\t- type: {}".format(type(res)))
            print("\t- content: {}".format(res))
            print("\t- utf8 content: {}".format(res.decode('utf-8')))
    except URLError as e:
        if hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        elif hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
