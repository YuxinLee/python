#coding=utf-8

import networkx as nx
from Demo1 import Host

def get_vm(vm_name, vm_list):
    for i in vm_list:
        if(i.get_vm_name() == vm_name):
            return i

def get_link_bandwidth_consumption(g, vm1_name, vm2_name, bandwidth, vm_list):
    vm1 = get_vm(vm1_name, vm_list)
    vm2 = get_vm(vm2_name, vm_list)
    host1 = vm1.get_vm_host()
    host2 = vm2.get_vm_host()
    if(list(nx.all_simple_paths(g, host1.get_host_name(), host2.get_host_name()))==[]):
        return 0
    link_list = list(nx.all_simple_paths(g, host1.get_host_name(), host2.get_host_name()))[0]
    link_number = len(link_list)
    total_link_bandwidth = (link_number - 1) * bandwidth
    for i in range(0, link_number-1, 1):
        g[link_list[i]][link_list[i+1]]["bandwidth"] = g[link_list[i]][link_list[i+1]]["bandwidth"] - bandwidth

    return total_link_bandwidth


def get_datacenter_link_bandwidth_consumption(g, vm_vm_bandwidth, vm_list):
    total_datacenter_link_bandwidth_consumption = 0
    for key in vm_vm_bandwidth:
        vm_vm = key.split(":")
        vm1_name = vm_vm[0]
        vm2_name = vm_vm[1]
        bandwidth = vm_vm_bandwidth[key]
        total_datacenter_link_bandwidth_consumption = total_datacenter_link_bandwidth_consumption + get_link_bandwidth_consumption(g, vm1_name, vm2_name, bandwidth, vm_list)
    return total_datacenter_link_bandwidth_consumption





