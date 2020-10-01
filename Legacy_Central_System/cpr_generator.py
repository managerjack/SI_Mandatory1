import xml.etree.ElementTree as et
import msgpack
import os 
import random
from nemId_generator import NemIdGenerator as ng

####################################
# Save data in msgpack files

def save_msgpack(person):

    with open(str(cpr) + ".msgpack", "ab") as msgwrite:
            pack = msgpack.packb(person)
            msgwrite.write(pack)
            msgwrite.close()

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

        root =  et.Element("Person")
        et.SubElement(root, "FirstName").text = per_obj['FirstName']
        et.SubElement(root, "LastName").text = per_obj['LastName']
        et.SubElement(root, "CprNumber").text = per_obj['CprNumber']
        et.SubElement(root, "Email").text = per_obj['Email']

        xml_string = et.tostring(root).decode()

        save_msgpack(per_obj)
        nem_request.send_request(xml_string)      



    
