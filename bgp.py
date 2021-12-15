import requests
import json
from colorama import Fore
import os 
from platform import platform
import sys

def baner():
    plat = platform()
    if "Windows" in plat:
        os.system("cls")
    else:
        os.system("clear")
    print(Fore.LIGHTRED_EX+ """
    coded by  : matin nouriyan
    ███╗   ███╗ █████╗ ████████╗██╗████████╗ █████╗ ███╗   ██╗██╗██╗   ██╗███╗   ███╗
    ████╗ ████║██╔══██╗╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║██║██║   ██║████╗ ████║
    ██╔████╔██║███████║   ██║   ██║   ██║   ███████║██╔██╗ ██║██║██║   ██║██╔████╔██║
    ██║╚██╔╝██║██╔══██║   ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║██║   ██║██║╚██╔╝██║
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║   ██║   ██║  ██║██║ ╚████║██║╚██████╔╝██║ ╚═╝ ██║
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝     ╚═╝ 
                                             
    """)
    print(Fore.LIGHTBLUE_EX+"""
        Enter your search format: 
        ASN = 1
        ip = 2
        perfix = 3     
                   
          """)



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
    get_rec_type.select = request_type

baner()


get_rec_type()
format = get_rec_type.select


if format == 1:
    format_type="asn"
elif format == 2:
    format_type ="ip"
elif format== 3:
    format_type="perfix"
else:
    print("Error")
    sys.exit()






api = ("https://api.bgpview.io/{format}/{value}").format(format=format_type,value=714)
api2 = requests.get(api)
print(api2.text)