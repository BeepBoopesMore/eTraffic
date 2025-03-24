from eTraffic import Router
import requests
import json
from eTraffic import DHCP_Server 

# To do

# -Subnetting Calculator based on multiple Routers 
# - VLSM calculator
# Subnet mask calculator
# OSPF path
#Command API eTraffic , send commands via an API
#Model LookUp


router1 = Router("192.168.1.136","John","aff","Cisco")




def model_lookup(model_number:str,vendor:str,api_key:str):
    print('later')




file_path = "../eTrafficApp/Router/dynamic_routing.json"
with open(file_path,"r") as file:
    data = json.load(file)
    print(data)








#Define the area you are trying to subnet
class Office():
    def __init__(self):
        () 