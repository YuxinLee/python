#coding=utf-8

import networkx as nx
import random
import numpy as np

migration_cost = 0.0

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

def update_host(vm_list, host):
    host.cpu_used = 0
    host.mem_used = 0
    for i in vm_list:
        if (i.hostname == host.name):
            cpu_used = host.cpu_used
            mem_used = host.mem_used
            vm_cpu = i.cpu
            vm_mem = i.mem
            host.cpu_used = cpu_used + vm_cpu
            host.mem_used = mem_used + vm_mem

def update_host_list(vm_list, host_list):
    for host in host_list:
        update_host(vm_list, host)

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

def migration_VMDM(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y):
    host = get_migration_VMDM_host(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
    host.status = "active"
    host_cpu_used = host.cpu_used
    host_mem_used = host.mem_used
    host.cpu_used = host_cpu_used + vm.cpu
    host.mem_used = host_mem_used + vm.mem
    vm.hostname = host.name
    # print("虚拟机", vm.name, "迁移到服务器", vm.hostname, "中")

def get_migration_VMDM_host(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y):
    placement_priority_list = get_placement_priority_list(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list,
                                                          x, y)
    if (not judge_bandwidth_threshold(host_link_list)):
        del avail_host_list[placement_priority_list.index(max(placement_priority_list))]
        del placement_priority_list[placement_priority_list.index(max(placement_priority_list))]
    max_placement_priority = max(placement_priority_list)
    max_placement_priority_index = placement_priority_list.index(max_placement_priority)
    host = avail_host_list[max_placement_priority_index]
    return host

"""
迁移虚拟机
"""
def vm_live_migration(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y):
    migration_VMDM(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)

def vm_live_migration_cost(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y):
    host = get_migration_VMDM_host(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
    min_link_free = 20
    # if(vm.hostname == host.name):
    #     return 0
    # path_list = get_path_list(g, vm.hostname, host.name)
    #
    # link_free_list = []
    # for i in range(len(path_list)-1):
    #     link_sum = get_link_sum(host_link_list, path_list[i], path_list[i+1])
    #     link_used = get_link_used(host_link_list, path_list[i], path_list[i+1])
    #     link_free = link_sum - link_used
    #     link_free_list.append(link_free)
    # min_link_free = min(link_free_list)
    vm_live_cost = vm.mem * 1.0 / min_link_free
    return vm_live_cost

def host_live_migration_cost(g, host, vm_list, vm_link_list, avail_host_list, host_link_list, x, y):
    host_live_migration_cost = 0.0
    vm_list_of_host = get_vm_list_of_host(vm_list, host)
    for vm in vm_list_of_host:
        cost = vm_live_migration_cost(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
        host_live_migration_cost = host_live_migration_cost + cost
    return host_live_migration_cost



# def del_low_resource_host(g, vm_list, vm_link_list, avail_host_list, host_link_list, x, y, low_resource_host_list):
#     global migration_cost
#     if (low_resource_host_list == []):
#         return
#     for i in range(len(low_resource_host_list)):
#         vm_list = get_vm_list_of_host(vm_list, low_resource_host_list[i])
#         for j in range(len(vm_list)):
#             vm_live_migration(g, vm_list[j], vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
#             migration_cost = migration_cost + vm_live_migration_cost(g, vm_list[j], vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
#         low_resource_host_list[i].status = "sleep"

def del_low_resource_host(g, d, low_resource_host_list, vm_list, vm_link_list,  host_link_list, x, y):
    global migration_cost
    if(low_resource_host_list == []):
        return
    for host in low_resource_host_list:
        # print(host.name)
        vm_list = get_vm_list_of_host(vm_list, host)
        for vm in vm_list:
            # print(vm.name)
            avail_host_list = d.get_avail_host_list()
            vm_live_migration(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
            cost = vm_live_migration_cost(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
            migration_cost = migration_cost + cost

        host.status = "sleep"

def get_host_down_probability(host):
    host_load = 0.8 * (host.cpu_used * 1.0 / host.cpu_sum) + 0.2 * (host.mem_used * 1.0 / host.mem_sum)
    host_down_probability = 1.0 / (1 + np.e ** ((-10)*host_load + 5))
    return host_down_probability

def del_candidate_host(g, d, vm_list, vm_link_list,  host_link_list, x, y, candidate_host_list):
    global migration_cost
    if (candidate_host_list == []):
        return
    for i in range(len(candidate_host_list)):
        candidate_host = candidate_host_list[i]
        host_down_probability = get_host_down_probability(candidate_host)
        avail_host_list = d.get_avail_host_list()
        host_down_cost = host_down_probability * \
                         host_live_migration_cost(g, candidate_host, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
        vm_list_of_host = get_vm_list_of_host(vm_list, candidate_host)
        vm_migration_cost_list = []
        for vm in vm_list_of_host:
            vm_migration_cost_list.append(vm_live_migration_cost(g, vm, vm_list, vm_link_list, avail_host_list, host_link_list, x, y))
        vms = vm_list_of_host[vm_migration_cost_list.index(max(vm_migration_cost_list))]
        if(max(vm_migration_cost_list) < host_down_cost):
            vm_live_migration(g, vms, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
            cost=vm_live_migration_cost(g, vms, vm_list, vm_link_list, avail_host_list, host_link_list, x, y)
            migration_cost = migration_cost + cost
# def del_candidate_host(candidate_host_list):
#     global migration_cost
#     if (candidate_host_list == []):
#         return
#     for host in candidate_host_list:
#         print(host.name)


def get_total_migration_cost():
    global migration_cost
    return migration_cost

def vm_resource_dynamic_change(vm_list):
    cpu_list = [1, 2, 4, 8, 12]  # cpu请求列表
    mem_list = [1, 2, 4, 8, 16]  # mem请求列表
    disk_list = [10, 40, 100, 200, 300]  # disk请求列表
    cpu = random.sample(cpu_list, 1)[0]
    mem = random.sample(mem_list, 1)[0]
    disk = random.sample(disk_list, 1)[0]
    for vm in vm_list:
        vm.cpu = cpu
        vm.mem = mem
        vm.disk = disk

def vm_link_dynamic_change(vm_link_list):
    bandwidth_list = [1, 5, 10, 20, 30]  # 带宽请求列表
    bandwidth = random.sample(bandwidth_list, 1)[0]
    for i in vm_link_list:
        i.bandwidth = bandwidth

