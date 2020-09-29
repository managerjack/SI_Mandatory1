import requests
import urllib.request

xml_file = """person.xml"""

header = {'Content-Type': 'application/xml'}

with open(xml_file) as xml:
    r = requests.post("http://localhost:8080/nemId", data = xml, headers = header)
    
print(r.content)
print(r.status_code)