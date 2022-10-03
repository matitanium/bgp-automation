
import os
try:
    import ipaddress
except:
    os.system("pip install ipaddress")
    import ipaddress
    
def Convert_ip(cidr):
    net = ipaddress.ip_network(cidr)
    iplist = []
    for i in net:
        iplist.append(i)
    return iplist