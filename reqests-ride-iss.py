#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

# notice we no longer need to import urllib.request or json
try:
    import os
    import requests
    # import zachrequests
except Exception as z:
    print("Oh i see you're trying to grab a module from team... go look at xyz location for that code!", z)
    exit()

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()


    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()


    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

if __name__ == "__main__":
    main()

