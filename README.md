# auto-read-dhcp-lease

## Usage
###use default dhcp lease file(/var/lib/dhcpd/dhcpd.leases)

python get_ip_mac_in_lease.py

###specify target dhcp lease file

python get_ip_mac_in_lease.py /path/to/dhcpd.leases

## NOTE
###dev under python 3.8.6 on centos7

###install requirements by using:

pip instsall -r requrirement.txt
