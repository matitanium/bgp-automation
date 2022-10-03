import sys
from module.eqnc import *
from colorama import Fore
from module.Cidr_to_ip import *

def start():
    
    baner()
    get_rec_type()
    format = get_rec_type.select
    if format == 1:
        format_type="domain"
    elif format== 2:
        format_type="prefix"
    elif format== 3:
        format_type="ip"
    elif format== 4:
        sys.exit("tnx")
    else:
        start()
        
        
    get_value(format_type)
    value_to_search = get_value.out





    # ip_file = open("./list/ip.txt","w+")
    if format_type=="domain":
        domain(search=value_to_search)




    elif format_type=="prefix":
        perfix(search=value_to_search)



    
    # elif format_type=="asn":
    #     pass
        
    
    
    
    
    
    elif format_type=="ip":
        ifip(value_to_search)
        print(ifip.asns)
        print("==============")
        perfix(search=ifip.perfix)
        print("ok in cidr-to-iplist txt")

            
        
    
            
    else:
        ifother(format_type,value_to_search)
        if ifother.status =="error":
            print("I Cant Find Your Query!  , Please Try again")
            sys.exit()
start()