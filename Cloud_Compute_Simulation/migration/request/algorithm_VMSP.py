#coding=utf-8
import networkx as nx
import random

#获取与服务器之间连接的接入交换机
def get_access_switch(g, host_name):
    for i in g.neighbors(host_name):
        return i

def get_path_list(g, node1_name, node2_name):
    node_link_list = list(nx.all_simple_paths(g, node1_name, node2_name))
    if(node_link_list == []):
        return
    node_list = node_link_list[0]
    return node_list

def update_node_bandwidth_used_node(host_link_list, node1_name, node2_name, bandwidth_used):
    for i in host_link_list:
        if ((i.node1_name == node1_name and i.node2_name == node2_name) or (
                i.node1_name == node2_name and i.node2_name == node1_name)):
            i.bandwidth_used = bandwidth_used


def update_host_link(g, vm_link_list, host_link_list):
    for i in range(len(vm_link_list)):
        vm1 = vm_link_list[i].vm1
        vm2 = vm_link_list[i].vm2
        bandwidth = vm_link_list[i].bandwidth
        vm1_hostname = vm1.hostname
        vm2_hostname = vm2.hostname
        node_link_list = list(nx.all_simple_paths(g, vm1_hostname, vm2_hostname))
        if (node_link_list == []):
            continue
        node_list = node_link_list[0]
        for i in range(0, len(node_list) - 1, 1):
            node1_name = node_list[i]
            node2_name = node_list[i + 1]
            bandwidth_used = get_link_used(host_link_list, node1_name, node2_name)
            bandwidth_used = bandwidth_used + bandwidth
            update_node_bandwidth_used_node(host_link_list, node1_name, node2_name, bandwidth_used)


def get_link_sum(host_link_list, node1_name, node2_name):
    for i in host_link_list:
        if((i.node1_name == node1_name and i.node2_name == node2_name) or (i.node1_name == node2_name and i.node2_name == node1_name)):
            return i.bandwidth_sum

def get_link_used(host_link_list, node1_name, node2_name):
    for i in host_link_list:
        if((i.node1_name == node1_name and i.node2_name == node2_name) or (i.node1_name == node2_name and i.node2_name == node1_name)):
            return i.bandwidth_used

def get_vm_list_of_host(vm_list, host):
    vm_list_of_host = []
    for i in vm_list:
        if (i.hostname == host.name):
            vm_list_of_host.append(i)
    return vm_list_of_host

def get_both_vm_badwidth(vm1, vm2, vm_link_list):
    for i in vm_link_list:
        if (((i.vm1.uuid == vm1.uuid) and (i.vm2.uuid == vm2.uuid)) or (
                (i.vm1.uuid == vm2.uuid) and (i.vm2.uuid == vm1.uuid))):
            return i.bandwidth

def get_vm_host_bandwidth(vm, host, vm_list, vm_link_list):
    vm_list_of_host = get_vm_list_of_host(vm_list, host)
    bandwidth = 0
    for i in vm_list_of_host:
        vm_vm_bandwidth = get_both_vm_badwidth(vm, i, vm_link_list)
        if(vm_vm_bandwidth == None):
            vm_vm_bandwidth = 0
        bandwidth = bandwidth + vm_vm_bandwidth
    return bandwidth

# 获取计算资源平衡度列表
def get_compute_resource_balance_list(vm, avail_host_list):
    compute_resource_balance_list = []
    for i in avail_host_list:
        host_cpu_used = i.cpu_used
        host_cpu_sum = i.cpu_sum
        host_mem_used = i.mem_used
        host_mem_sum = i.mem_sum
        cpu_balance = ((host_cpu_used * 1.0 / host_cpu_sum) - (vm.cpu * 1.0 / host_cpu_sum)) ** 2
        mem_balance = ((host_mem_used * 1.0 / host_mem_sum) - (vm.mem * 1.0 / host_mem_sum)) ** 2
        compute_resource_balance = ((cpu_balance + mem_balance) * 1.0 / 2) ** 0.5
        compute_resource_balance_list.append(compute_resource_balance)
    return compute_resource_balance_list

# 获取链路资源平衡度列表
def get_link_resource_balance_list(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list):
    link_resource_balance_list = []
    for i in avail_host_list:
        access_switch_name = get_access_switch(g, i.name)
        link_sum = get_link_sum(host_link_list, i.name, access_switch_name)
        link_used = get_link_used(host_link_list ,i.name, access_switch_name)
        vm_host_bandwidth = get_vm_host_bandwidth(vm, i, vm_list, vm_link_list)
        link_resource_balance = (link_used * 1.0 / link_sum) - (vm_host_bandwidth * 1.0 / link_sum)
        link_resource_balance_list.append(link_resource_balance)
    return link_resource_balance_list

"""
获取放置优先级列表，目前取权值为1：1     x和y表示权值
"""

def get_placement_priority_list(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list,  x, y):
    compute_resource_balance_list = get_compute_resource_balance_list(vm, avail_host_list)
    link_resource_balance_list = get_link_resource_balance_list(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list)
    placement_priority_list = []
    for i in range(len(compute_resource_balance_list)):
        placement_priority_list.append((x * compute_resource_balance_list[i]) + (y * link_resource_balance_list[i]))
    return placement_priority_list

def judge_bandwidth_threshold(host_link_list):
    flag = True
    for i in host_link_list:
        if(i.bandwidth_used * 1.0 / i.bandwidth_sum > 0.6):
            flag = False
            return flag
    return flag

def placement_VMSP(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y):
    placement_priority_list = get_placement_priority_list(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list,  x, y)
    if (not judge_bandwidth_threshold(host_link_list)):
        del avail_host_list[placement_priority_list.index(max(placement_priority_list))]
        del placement_priority_list[placement_priority_list.index(max(placement_priority_list))]
    max_placement_priority = max(placement_priority_list)
    max_placement_priority_index = placement_priority_list.index(max_placement_priority)
    host = avail_host_list[max_placement_priority_index]
    host_cpu_used = host.cpu_used
    host_mem_used = host.mem_used
    host.cpu_used = host_cpu_used + vm.cpu
    host.mem_used = host_mem_used + vm.mem
    vm.hostname = host.name
    print("虚拟机", vm.name, "放置在服务器", vm.hostname, "中")
