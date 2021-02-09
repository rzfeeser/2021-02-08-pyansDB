#!/usr/bin/python3
"""RESTful API client | RZFeeser@alta3.com"""

import requests # required to make API requests

MYAPI = "http://0.0.0.0:2224/astros"

def main():
    # send http GET request to MYAPI
    resp = requests.get(MYAPI)
    
    # display the HTTP resp code
    print(resp.status_code)
    
    # display json from the resp
    print(resp.json())
    
if __name__ == "__main__":
    main()

