import sys
from colorama import Fore
from platform import platform
import os
import requests
import json







def baner():
    plat = platform()
    if "Windows" in plat:
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.LIGHTRED_EX+ """
    coded by : matin nouriyan | instagram/github : matitanium
    ███╗   ███╗ █████╗ ████████╗██╗████████╗ █████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██║██║   ██║████╗ ████║
    ██╔████╔██║███████║   ██║   ██║   ██║   ███████║██╔██╗ ██║██║██║   ██║██╔████╔██║
    ██║╚██╔╝██║██╔══██║   ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║   ██║   ██║  ██║██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝                                      
    """)
    print(Fore.LIGHTBLUE_EX+"""
        Enter your search format:
        
         
        1 = information ghaternig by Company Name!...
        2 = Search by ip... 
        3 = Exit          
     """)







# get search type
def get_rec_type():
    try:
        request_type = int(input(Fore.MAGENTA+"[+] 1-3 =>"))
    except :
        print("just select 1-3!! - by :D")
        sys.exit()
    if 0<int(request_type)<4:
        pass
    else:
        print("just select 1-3!! - by :D")
        sys.exit()
    
    #number of selected option
    get_rec_type.select = request_type









#get target        
def getTarget(type2):
    if type2 == "ip":
        ip = input("[+] Enter Your IP to Search... Examlpe(0.0.0.0) =>")
        getTarget.out = ip
    elif type2 == "domain":
        dom = input("[+] information ghaterin[*] #_# Enter Company Name to Search... Examlpe(microsoft) => ")
        getTarget.out = dom




    
    

 
    


#if selected 4 search by ip
def ifip(ip):
    api = ("https://api.bgpview.io/ip/{i}").format(i=ip)
    print("======================================")
    string_output = requests.get(api).text
    json_output  = json.loads(string_output)
    #read json status for find
    status = json_output["status"]
    if status =="error":
        print("I Cant Find Your Query!  , Please Try again")
        sys.exit()
        
        
    # ASN
    ifip.asns = json_output["data"]["prefixes"][0]["asn"]["asn"]
    #company name 
    ifip.compayName = json_output["data"]["prefixes"][0]["asn"]["description"]
    #perfix
    ifip.perfix= json_output["data"]["prefixes"][0]["prefix"]
    








#convert asn to cidr list
def asnToPerfix(asn):
    url = "https://api.bgpview.io/asn/{a}/prefixes".format(a=asn)
    request = requests.get(url).text
    #convert request plain to json 
    json_request = json.loads(request)
        #read json status for find
    status = json_request["status"]
    if status =="error":
        print("I Cant Find Your Query!  , Please Try again")
        sys.exit()
    perfixes = json_request["data"]["ipv4_prefixes"]
    for i in perfixes:
        print(i["prefix"],": ",i["description"])










def ifdomin(domain):
    api = ("https://api.bgpview.io/search?query_term={dom}#results-v4").format(dom=domain)
    print("======================================")
    string_output = requests.get(api).text
    json_output  = json.loads(string_output)
    status = json_output["status"]
    asns = json_output["data"]["asns"]
    perfix = json_output["data"]["ipv4_prefixes"]
    if status =="error":
        print("I Cant Find Your Query!  , Please Try again")
        sys.exit()
    for i in perfix:
        print(Fore.GREEN+i["prefix"],": ",i["description"])

    print("====================")
    print(asns)



