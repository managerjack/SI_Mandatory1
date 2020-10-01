import xml.etree.ElementTree as et
import msgpack
import os 
import random
from nemId_generator import NemIdGenerator as ng


def save_msgpack(person):
    ''' Save person data in msgpack files

    Args:
        person (dict): Personal information to be saved. 
    '''
    with open(str(person['CprNumber']) + ".msgpack", "ab") as msgwrite:
            pack = msgpack.packb(person)
            msgwrite.write(pack)
            msgwrite.close()

def create_xml(person):
    ''' This function will construct an xml object.

    Args:
        person (dict): Personal information
    
    Returns:
        xml_person (str): String representation of xml person file.
    '''
    root = et.Element("Person")
    et.SubElement(root, "FirstName").text = person['FirstName']
    et.SubElement(root, "LastName").text = person['LastName']
    et.SubElement(root, "CprNumber").text = person['CprNumber']
    et.SubElement(root, "Email").text = person['Email']

    xml_person = et.tostring(root).decode()

    return xml_person

def create_nemIds():
    ''' Will initiate the creation of new NemID users.
    '''
    with open ("../Main_System/people.csv") as csvfile:
        nem_request = ng()
        reader = csvfile.readlines()[1:]

        for person in reader:      
            cpr = person
            cpr = cpr.replace('-', '')
            cpr = cpr.split(',')[3]
            
            for number in range(4):
                n = random.randint(0, 9)
                cpr = cpr + str(n)
            
            per_obj = {
                "FirstName": person.split(',')[0],
                "LastName": person.split(',')[1],
                "CprNumber": cpr,
                "Email": person.split(',')[2],
                "Country": person.split(',')[6],
                "Phone": person.split(',')[4],
                "Address": person.split(',')[5]
            }

            xml = create_xml(per_obj)

            created = nem_request.send_xml(xml)
            
            if created:
                save_msgpack(per_obj)

if __name__ == '__main__':
    create_nemIds()