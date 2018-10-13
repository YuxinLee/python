#coding=utf-8

from Demo1 import DataCenter

#处于活跃状态的服务器
alive_host_list = DataCenter.get_alive_host_list()
#DataCenter.init_datacenter()
sleep_host_list = DataCenter.get_sleep_host_list()
# print(alive_host_list)
# print(sleep_host_list)

# 得到可用cpu资源主机列表，设定的资源阈值为0.8
def get_availiable_cpu_host_list(vm_cpu):
    availiable_cpu_host_list = []
    for i in range(len(alive_host_list)):
        host_cpu_used = alive_host_list[i].get_host_cpu_used()
        host_cpu_sum = alive_host_list[i].get_host_cpu_sum()
        if((vm_cpu+host_cpu_used)*1.0/host_cpu_sum<=0.8):
            availiable_cpu_host_list.append(alive_host_list[i])
    return availiable_cpu_host_list

#print(get_availiable_cpu_host_list(1))

# 得到可用mem资源主机列表，设定的资源阈值为0.8
def get_availiable_mem_host_list(vm_mem):
    availiable_mem_host_list = []
    for i in range(len(alive_host_list)):
        host_mem_used = alive_host_list[i].get_host_mem_used()
        host_mem_sum = alive_host_list[i].get_host_mem_sum()
        if ((vm_mem + host_mem_used) * 1.0 / host_mem_sum <= 0.8):
            availiable_mem_host_list.append(alive_host_list[i])
    return availiable_mem_host_list

# 得到满足cpu和mem的可用资源主机列表，设定的资源阈值为0.8
def get_availiable_all_resource_host_list(vm_cpu, vm_mem):
    availiable_cpu_host_set = set(get_availiable_cpu_host_list(vm_cpu))
    availiable_mem_host_set = set(get_availiable_mem_host_list(vm_mem))
    availiable_all_resource_host_set = availiable_cpu_host_set & availiable_mem_host_set
    availiable_all_resource_host_list = list(availiable_all_resource_host_set)

    if availiable_all_resource_host_list == []:
        sleep_host_list[0].set_host_status("alive")
        availiable_all_resource_host_list.append(sleep_host_list[0])
    return availiable_all_resource_host_list

#print(get_availiable_all_resource_host_list(1,1))

# 获取资源融合度的列表
def get_resource_balance_list(vm_cpu, vm_mem):
    resource_balance_host_list = []
    availiable_all_resource_host_list = get_availiable_all_resource_host_list(vm_cpu, vm_mem)
    availiable_all_resource_host_number = len(get_availiable_all_resource_host_list(vm_cpu, vm_mem))
    for i in range(availiable_all_resource_host_number):
        host_cpu_used = availiable_all_resource_host_list[i].get_host_cpu_used()
        host_cpu_sum = availiable_all_resource_host_list[i].get_host_cpu_sum()
        host_mem_used = availiable_all_resource_host_list[i].get_host_mem_used()
        host_mem_sum = availiable_all_resource_host_list[i].get_host_mem_sum()

        cpu_balance = ((host_cpu_used * 1.0 / host_cpu_sum) - (vm_cpu * 1.0 / host_cpu_sum)) ** 2
        mem_balance = ((host_mem_used * 1.0 / host_mem_sum) - (vm_mem * 1.0 / host_mem_sum)) ** 2
        vm_host_balance = (cpu_balance + mem_balance) ** 0.5

        resource_balance_host_list.append(vm_host_balance)
    return resource_balance_host_list

def get_max_resource_balance(vm_cpu, vm_mem):
    resource_balance_host_list = get_resource_balance_list(vm_cpu, vm_mem)
    resource_balance_max_host = max(resource_balance_host_list)
    return resource_balance_max_host

#获取资源融合度最高的主机
def get_best_resource_balance_host(vm_cpu, vm_mem):
    resource_balance_host_list = get_resource_balance_list(vm_cpu, vm_mem)
    resource_balance_max_host = max(resource_balance_host_list)
    resource_balance_max_host_index = resource_balance_host_list.index(resource_balance_max_host)
    if(resource_balance_max_host == 0):
        sleep_host_list[0].set_host_status("alive")
        return sleep_host_list[0]
    return get_availiable_all_resource_host_list(vm_cpu, vm_mem)[resource_balance_max_host_index]

#print(get_best_resource_balance_host(1,1))
#print(get_availiable_cpu_host_list(1))

def algorithm_single_vm(vm_cpu, vm_mem, vm_disk):
    host = get_best_resource_balance_host(vm_cpu, vm_mem)
    host_cpu_used = host.get_host_cpu_used()
    host.set_host_cpu_used(vm_cpu+host_cpu_used)
    host_mem_used = host.get_host_mem_used()
    host.set_host_mem_used(vm_mem+host_mem_used)

def algorithm_more_vm(vm_cpu, vm_mem, vm_disk,host):
    host_cpu_used = host.get_host_cpu_used()
    host.set_host_cpu_used(vm_cpu + host_cpu_used)
    host_mem_used = host.get_host_mem_used()
    host.set_host_mem_used(vm_mem + host_mem_used)