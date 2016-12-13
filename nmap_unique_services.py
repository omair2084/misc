#Print unique services found on the network
#using the xml output from nmap
#nmaprun > host > ports > port > service


import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('basic_scans.xml').getroot()
fe = open("services_only.txt","w")
for elem in e.findall('host/ports/port/service'):
    z = str(elem.get('product'))+"\n"
	fe.write(z)

f = open("services_only.txt", "r")
lines = set(f.readlines())
print ''.join(lines)


