import requests
import urllib.request

class NemIdGenerator:
    ADDRESS = "http://localhost"
    PORT = 8080
    ENDPOINT = "/nemId"

    def send_request(self, xml_payload):
        header = {'Content-Type': 'application/xml'}
        res = requests.post(f"{self.ADDRESS}:{self.PORT}{self.ENDPOINT}", data = xml_payload, headers = header)

        print(f"\rSTATUS CODE: {res.status_code}\r")
        print(res.content)