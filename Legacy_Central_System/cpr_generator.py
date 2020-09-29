import xml.etree.ElementTree as et
import msgpack
import os 
import random

####################################
# Save data in msgpack files

def save_msgpack(person):
    pass

with open ("../Main_System/people.csv") as csvfile:
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
            "CprNumber": person.split(',')[3],
            "Email": person.split(',')[2]
        }

        root =  et.Element("Person")
        et.SubElement(root, "FirstName").text = per_obj['FirstName']
        et.SubElement(root, "LastName").text = per_obj['LastName']
        et.SubElement(root, "CprNumber").text = per_obj['CprNumber']
        et.SubElement(root, "Email").text = per_obj['Email']
        
        tree = et.ElementTree(root)
        tree.write('person.xml') #, encoding='UTF-8', xml_declaration=True)

        save_msgpack(per_obj)
        



    
