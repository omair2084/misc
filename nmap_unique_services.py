#Python3
#Print unique services found on the network
#using the xml output from nmap
#nmaprun > host > ports > port > service

import xml.etree.ElementTree
import sys

if len(sys.argv) != 2:
    print("[-] Supply nmap .xml outputfile")
    print("Help: %s scanOutput.xml" % sys.argv[0])
    sys.exit(-1)

e = xml.etree.ElementTree.parse(sys.argv[1]).getroot()
fe = open("services_only.txt","w")
for elem in e.findall('host/ports/port/service'):
    z = str(elem.get('product'))+"\n"
    fe.write(z)

f = open("services_only.txt", "r")
lines = set(f.readlines())
print (''.join(lines))


