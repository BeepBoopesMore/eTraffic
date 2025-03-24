import re

import unicodedata

#Using this for doing the data mostly 

#Vlan 


with open("testingdata.txt","r") as file:
    data = file.read()
    pattern_vlan_name = r'^\d+\s+([A-Za-z0-9\s]+)\s+(\w+)\s+'
    pattern = r'^\d+\s+[a-zA-Z0-9\s]+(?:\s+active)?\s+([a-zA-Z0-9/,\s]+)'

 


matches_vlan_name = re.findall(pattern_vlan_name, data, re.MULTILINE)
matches_vlan_ports = re.findall(pattern, data, re.MULTILINE)

vlans_status = []
vlans_names = []
vlans_ports = []
#Going Through Matches vlan
for match in matches_vlan_name:
    #Statuses
    vlans_status.append(match[1])
    #Names 
    match  = "".join(match[0].split())
    vlans_names.append(match)


def spanning_tree():
    with open("testingdata.txt","r") as file:
        data = file.read()
        pattern = ""


print(vlans_status)
print(vlans_names)
