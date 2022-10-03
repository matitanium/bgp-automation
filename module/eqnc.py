import sys
from colorama import Fore
from platform import platform
import os
import requests
import json
from module.Cidr_to_ip import *


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
        2 = Cidr/prefix to ip list...
        3 = Search by ip... 
        4 = Exit          
     """)

        
def get_value(formato):
    a = formato
    if a == "asn":
        asn = input("[+] Enter Your ASN to Search... Examlpe(0000) =>")
        get_value.out = asn
    elif a == "ip":
        ip = input("[+] Enter Your IP to Search... Examlpe(0.0.0.0) =>")
        get_value.out = ip
    elif a == "prefix":
        perfix = input("[+] Enter Your Cidr/Perfix to Convert... Examlpe(0.0.0.0/24) => ")
        get_value.out = perfix
    elif a == "domain":
        dom = input("[+] information ghaterin[*] #_# Enter Company Name to Search... Examlpe(microsoft) => ")
        get_value.out = dom



def get_rec_type():
    try:
        request_type = int(input(Fore.MAGENTA+"[+] 1-5 =>"))
    except :
        print("just select 1-5!! - by :D")
        sys.exit()
    if 0<int(request_type)<6:
        pass
    else:
        print("just select 1-5!! - by :D")
        sys.exit()
    get_rec_type.select = request_type



    
    
def ifdomin(domain):
    api = ("https://api.bgpview.io/search?query_term={dom}#results-v4").format(dom=domain)
    print("======================================")
    string_output = requests.get(api).text
    json_output  = json.loads(string_output)
    ifdomin.status = json_output["status"]
    ifdomin.asns = json_output["data"]["asns"]
    ifdomin.ip = json_output["data"]["ipv4_prefixes"]
 
 
 
    


#if selected 4 search by ip
def ifip(ip):
    api = ("https://api.bgpview.io/ip/{i}").format(i=ip)
    print("======================================")
    string_output = requests.get(api).text
    json_output  = json.loads(string_output)
    status = json_output["status"]
    if status =="error":
        print("I Cant Find Your Query!  , Please Try again")
        sys.exit()
    ifip.asns = json_output["data"]
    ifip.perfix= json_output["data"]["prefixes"][0]["prefix"]
    




def ifother(typee,value):
    api = ("https://api.bgpview.io/{format}/{value}").format(format=typee,value=value)
    print("======================================")
    string_output = requests.get(api).text
    json_output  = json.loads(string_output)
    ifother.status = json_output['status']
    print(json_output)
     


#convert perfix to ip list
def perfix(search):
    cidr = Convert_ip(search)
    ip_file = open("./Cidr-to-ip/Cidir-to-ip.txt","w+")
    for i in cidr:
        ip_file.write(str(i)+"\n")
    print(Fore.GREEN+"succesfuly convert. You can see output in Cidr-to-ip folder")



#search by company name
def domain(search):
    ifdomin(search)
    if ifdomin.status =="error":
        print("I Cant Find Your Query!  , Please Try again")
        sys.exit()
    else: 
        asns = []
        asn_file= open("./information ghatering/asns.txt","a+")
        ip = []
        prefix = []
        prefix_file = open("./information ghatering/prefix.txt","a+")
        ifdomin(search)
        asn_file.write("\n asns for {a} search \n \n ".format(a=search))
        prefix_file.write("\n Prefix for {a} search \n \n".format(a=search))
        for i in ifdomin.asns:
            asns.append(str(i["asn"])+" For this company=> "+str(i["description"]))
        asns = list(dict.fromkeys(asns))
        for f in asns:
            asn_file.write(f+"\n")
        for i in ifdomin.ip:
            ip.append(i["ip"])
        ip = list(dict.fromkeys(ip)) 
        for i in ifdomin.ip:
            prefix.append(str(i["prefix"])+" For this company=> = "+str(i["description"]))
            # parent_prefix.write(str(i['prefix'])+" decription =  "+str(i['description'])+"\n")
        prefix = list(dict.fromkeys(prefix)) 
        for f in prefix:
            prefix_file.write(f+"\n") 
        print(Fore.GREEN+"succesfully scanning... result in information ghathering directory")
            

   