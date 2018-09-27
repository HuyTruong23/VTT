#!/usr/bin/env python2
import fire
import os
from scapy.all import *

def pkt_sniff(interface=None, protocol="ip", count=None):
    sniff(iface=interface, prn=lambda x : x.show(), filter=protocol, store=0, count=count)

def main():
    fire.Fire(pkt_sniff)

if __name__ == '__main__':
    main()