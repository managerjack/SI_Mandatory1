import requests
import urllib.request


class NemIdGenerator:
    ''' This class is for sending a post message with a xml payload
    
    Attributes:
        __ADDRESS (str): Default server address.
        __PORT (int): Default server port.
        __ENDPOINT (str): Default endpoint.
        __default_address (str): Default address, port and endpoint.
    '''

    __ADDRESS = "http://localhost"
    __PORT = 8080
    __ENDPOINT = "/nemId"

    def __init__(self):
        self.__default_address = f"{self.__ADDRESS}:{self.__PORT}{self.__ENDPOINT}"

    def send_xml(self, xml_payload, address = None):
        ''' Send POST message with xml as payload to provided address.
        
        Args:
            xml_payload (str) xml to send as POST payload to server.
            address (str, optional) address to send POST message to.
        
        Returns:
            Boolean wether nemid was created or not.
        '''
        address = address if address else self.__default_address
        print("\nSending xml to '{}'...".format(address))
        
        header = {'Content-Type': 'application/xml'}
        res = requests.post(address, data = xml_payload, headers = header)

        print(f"STATUS CODE: {res.status_code}")
        print(res.content.decode('UTF-8'))

        return True if res.status_code == 200 else False

if __name__ == "__main__":
    n = NemIdGenerator()
    print(n.__doc__)
    print(n.send_xml.__doc__)
