import json
import requests
import os
from time import sleep



#Testing for the dynamic protocols 
file_path = input("path:")
with open(file_path,"r") as file:
    data = json.load(file)
    protocols = data["Protocols"]
    used_protocol =  protocols[0]
    protocol = used_protocol["dynamic_protocol"]
    if protocol == "OSPF":
        area = used_protocol["area"]
        network =  used_protocol["network"]
        process_id  = used_protocol["process_id"]
        reference_bandwidth = used_protocol["reference_bandwidth_value"]
        passive_interfaces =  used_protocol["passive_interfaces"]
        if reference_bandwidth == "Default":
            reference_bandwidth_used = 100
            command = "enable && configure terminal &&  router ospf " + str(process_id) + "&& auto-cost reference-bandwith " + str(reference_bandwidth_used) + " && network " + network +   " " + str(area) + " && exit && exit && write"
        elif reference_bandwidth >= 0:
            reference_bandwidth_used = reference_bandwidth
            command = "enable && configure terminal &&  router ospf " + str(process_id) + "&& auto-cost reference-bandwith " + str(reference_bandwidth_used) + " && network " + network +   " " + str(area) + " && exit && exit && write"
        else:
            print("!!! PLEASE USE DEFAULT OR A VALUE !!!")


        for item in passive_interfaces:
            command = "enable && configure terminal && router ospf " + str(process_id) + "&& passive-interface " + item   

    elif protocol == "EIGRP":
        astronomous_system = used_protocol["AS"]
        bool =  used_protocol["auto_summary"]
        network  = used_protocol["network"]
        passive_interfaces = used_protocol["passive_interfaces"]
        if bool == "True":
            command1 = "en && conf t && router eigrp " + astronomous_system + " && network " + network + " &&  auto-summary " + " && exit && exit && wr"
            for interface in passive_interfaces:
                command2 = "en && conf t && router eigrp " + astronomous_system + " && passive_interface " + interface 
                command3 = "en && wr"
        elif bool == "False":
            command4 = "en && conf t && router eigrp " + astronomous_system + " && network " + network  + " && exit && exit && wr"
            for interface in passive_interfaces:
                command5 = "en && configure terminal  && router eigrp " + astronomous_system + " && passive_interface " + interface 
                command6 = "en && write"
        else:
            print("!!! PLEASE INSERT TRUE OR FALSE !!!")
    
    elif protocol == "RIP":
        version = used_protocol["version"]
        auto_summary = used_protocol["auto_summary"]
        network = used_protocol["network"]

        if auto_summary == "True":
            command = "enable && configure terminal && router rip && auto-summary  " + " && network " + network + " && version " + version + " && exit && exit && write " 
        


        elif auto_summary == "False":
            command = "enable && configure terminal && router rip && no auto-summary "  + " && network " + network + " && version " + version + " && exit && exit && write "
            

        else:
            print("!!! PLEASE INSERT TRUE OR FALSE !!!")
    
    else:
        print("!!!PLEASE INSERT A CORRECT PROTOCOL OR  MAKE SURE THAT IT IS IN FULL CAPS!!!")
 






#Testing 

