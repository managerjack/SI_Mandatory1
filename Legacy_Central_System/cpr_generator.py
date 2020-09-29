from xml.dom import minidom
import os 
import random

with open ("../Main_System/people.csv") as csvfile:
    reader = csvfile.readlines()[1:]
    for person in reader:  
        
        cpr = person
        cpr = cpr.replace('-', '')
        cpr = cpr.split(',')[3]

        for number in range(4):
            n = random.randint(0, 9)
            cpr = cpr + str(n)
        
        #print(cpr)

        root = minidom.Document()

        xml = root.createElement('Person')
        root.appendChild(xml)

        productChild = root.createElement('FirstName')
        productChild.setAttribute('', person.split(',')[0])
                
        productChild2 = root.createElement('LastName')
        productChild2.setAttribute('', person.split(',')[1])

        productChild3 = root.createElement('CprNumber')
        productChild3.setAttribute('', cpr.split(',')[0])

        xml.appendChild(productChild)
        xml.appendChild(productChild2)
        xml.appendChild(productChild3)

        xml_str = root.toprettyxml(indent="\t")

        person_file_xml = "person.xml"

        with open(person_file_xml, "a", newline='') as f:
            f.writelines(xml_str)
        



    
