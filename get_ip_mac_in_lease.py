import sys
from  iscdhcpleases import Lease, IscDhcpLeases

def get_ip_mac_list(lease_file, valid=True):
    ip_mac_info_list = []
    leases = IscDhcpLeases(dhcp_lease_file)           #如果要处理gzip的lease file，leases = IscDhcpLeases('/path/to/dhcpd.leases', True) 
    #lease_obj_list = leases.get()
    #获取lease file中valid lease，默认情况
    if valid:
        leases_dict = leases.get_current()             #lease的binding state是active的且lease没过期才会被返回。返回值是dict，key是mac，value是lease obj
        leases_obj_list = leases_dict.values()
    #获取lease file中所有lease
    else:
        leases_obj_list = leases.get()                 #返回lease file中全部lease。目前__main__中没有方式可以选到这里

    for lease in leases_obj_list:
        ip_mac_info_list.append([lease.ip, lease.ethernet])

    return ip_mac_info_list

if __name__ == "__main__":
    #determine target dhcp lease file
    if len(sys.argv) > 1:
        dhcp_lease_file = sys.argv[1]

    else:
        #dhcp_lease_file = '/root/dhcpd.leases'
        dhcp_lease_file = "/var/lib/dhcpd/dhcpd.leases"

    try:
        ip_mac_list = get_ip_mac_list(dhcp_lease_file)

    except Exception as e:
        print(f"###Exception encountered, details is: {e}")

    #按ip递增排序
    ip_mac_list_sorted = sorted(ip_mac_list, key = lambda item:item[0])
    print(ip_mac_list_sorted)
