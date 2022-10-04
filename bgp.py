import sys
from module.eqnc import *
from colorama import Fore



#run banner 
baner()      
#ask for option
get_rec_type()
#number of option
format = get_rec_type.select #first entered number


if format == 1:
    format_type="domain"
elif format== 2:
    format_type="ip"
elif format== 3:
    sys.exit("tnx")
    
#get target and target type for ask    
getTarget(format_type)
#recived target
value_to_search = getTarget.out



if format_type=="domain":
    domain(search=value_to_search)

elif format_type=="ip":
    ifip(value_to_search)
    print(Fore.GREEN+"Asn: ",ifip.asns)
    print("Cidr: ",ifip.perfix)
    print("Company description: ",ifip.compayName)
    print("==============")
    wider = input("Do you need a wider scan?(y/n): ")
    wider = wider.lower()
    if wider == "y":
        asnToPerfix(ifip.asns)
    else:
        sys.exit()
    # perfix(search=ifip.perfix)

        
        
    
            
