import xml.etree.ElementTree as ET

tree = ET.parse(input("enter file path :"))

for e in tree.findall('host'):
    x = ""
    services = set()
    print("host:",e.find('address').items()[0][1])
    print("ports:")
    for port in e.find('ports').findall('port'):
        print(port.items()[1][1])
        try:
            if len(port.find('service').items()[1][1]) <= 40:
                services.add(port.find('service').items()[1][1])
        except AttributeError:
            pass
    print("\nidentified services")
    for val in services:
        print(val)
    print("=======")
 