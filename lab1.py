

import ifcfg
import json

for name, interface in ifcfg.interfaces().items():
    # do something with interface
    print "\n"
    print "Name: " + interface['device']
    print "IPv4: " + interface['inet']         # First IPv4 found
    print "" + str(interface['inet4'])        # List of ips
    print "IPv6: " + str(interface['inet6'])
    print "Netmask: " + interface['netmask']
    # print interface['broadcast']

default = ifcfg.default_interface()
