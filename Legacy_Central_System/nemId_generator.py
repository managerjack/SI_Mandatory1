import requests
import urllib.request

xml = """<?xml version='1.0' encoding='utf-8'?><a>6</a>"""

headers = {'Content-Type': 'person.xml'}

#This is a change
#x = requests.get('http://localhost:8080/nemID')
#print(x.status_code)

requests.post('http://localhost:8080/nemID', data={xml})

