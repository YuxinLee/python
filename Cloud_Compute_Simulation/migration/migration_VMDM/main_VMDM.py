#coding=utf-8

"""
用户请求的资源为：虚拟机列表(vm_list)， 带宽列表(vm_link_list)
遍历每一个用户
    输入：每一个用户的虚拟机列表和带宽列表
    输出：服务器的资源使用情况，虚拟机放置情况，功耗以及链路消耗
"""
from migration.request import service
from migration.request import datacenter
from migration.request import algorithm_VMSP
from migration.request import algorithm_Random
from migration.goal_function import power_consumption
from migration.goal_function import bandwidth_consumption
from migration.goal_function import active_host_number
from migration.goal_function import migration_cost
from migration.migration_VMDM import result_VMDM
from migration.migration_VMDM import algorithm_VMDM
import time
import uuid
import numpy as np
import random



result_VMDM.create_table_result()

# migration_cost = 0.0

def get_low_resource_host_list(d):
    active_host_list = d.get_active_host_list()
    low_resource_host_list = []
    for i in active_host_list:
        if ((i.cpu_used * 1.0 / i.cpu_sum) < 0.2 and (i.mem_used * 1.0 / i.mem_sum) < 0.2):
            low_resource_host_list.append(i)
    return low_resource_host_list

def deal_low_resource_host_list(d, vm_list):
    global migration_cost
    low_resource_host_list = get_low_resource_host_list(d)
    if (low_resource_host_list == []):
        return
    for host in low_resource_host_list:
        vm_list_of_host = get_vm_list_of_host(vm_list, host)
        for vm in vm_list_of_host:
            vm_live_migration(d, vm)
            cost = get_vm_migration_cost(vm)
            migration_cost = migration_cost + cost
        host.status = "sleep"

def deal_candidate_host_list(d, vm_list):
    candidate_host_list = get_candidate_host_list(d)
    global migration_cost
    if (candidate_host_list == []):
        return
    for host in candidate_host_list:
        host_migration_cost = get_host_migration_cost(vm_list, host)
        host_down_probability = get_host_down_probability(host)
        host_down_cost = host_down_probability * host_migration_cost
        vm_list_of_host = get_vm_list_of_host(vm_list, host)
        vm_migration_cost_list = []

        for vm in vm_list_of_host:
            vm_migration_cost_list.append(get_vm_migration_cost(vm))
        vm_migration_cost_min = min(vm_migration_cost_list)
        vm_migration_cost_index = vm_migration_cost_list.index(vm_migration_cost_min)
        vms = vm_list_of_host[vm_migration_cost_index]
        if (vm_migration_cost_min < host_down_cost):
            vm_live_migration(d, vms)
            cost = get_vm_migration_cost(vms)
            migration_cost = migration_cost + cost
def get_vm_placement_priority_host(d, vm):
    vm_placement_priority_host_list = []
    avail_host_list = get_avail_host_list(d, vm)
    for host in avail_host_list:
        host_cpu_used = host.cpu_used
        host_cpu_sum = host.cpu_sum
        host_mem_used = host.mem_used
        host_mem_sum = host.mem_sum
        cpu_balance = ((host_cpu_used * 1.0 / host_cpu_sum) - (vm.cpu * 1.0 / host_cpu_sum)) ** 2
        mem_balance = ((host_mem_used * 1.0 / host_mem_sum) - (vm.mem * 1.0 / host_mem_sum)) ** 2
        vm_host_balance = ((cpu_balance + mem_balance) /2.0 )** 0.5
        vm_placement_priority_host_list.append(vm_host_balance)
    vm_placement_priority_host_max = max(vm_placement_priority_host_list)
    vm_placement_priority_host_index = vm_placement_priority_host_list.index(vm_placement_priority_host_max)
    return avail_host_list[vm_placement_priority_host_index]


def get_link_free():
    return 20
def get_candidate_host_list(d):
    active_host_list = d.get_active_host_list()
    candidate_host_list = []
    for i in active_host_list:
        if ((i.cpu_used * 1.0 / i.cpu_sum) > 0.2 and (i.mem_used * 1.0 / i.mem_sum) > 0.2):
            candidate_host_list.append(i)
    return candidate_host_list

def get_avail_host_list(d,vm):
    avail_host_list = []
    active_host_list = d.get_active_host_list()
    sleep_host_list = d.get_sleep_host_list()
    if(active_host_list == []):
        host = sleep_host_list[0]
        host.status = "active"
        active_host_list.append(host)
    for i in active_host_list:
        host_cpu_used = i.cpu_used
        host_cpu_sum = i.cpu_sum
        host_mem_used = i.mem_used
        host_mem_sum = i.mem_sum
        if ((( vm.cpu + host_cpu_used) * 1.0 / host_cpu_sum <= 0.6) and (( vm.mem + host_mem_used) * 1.0 / host_mem_sum <= 0.6)):
            avail_host_list.append(i)
    if (avail_host_list == []):
        temp_list = d.get_sleep_host_list()
        temp_list[0].status = "active"
        avail_host_list.append(temp_list[0])
    return avail_host_list



def main():
    """
    初始化用户请求的资源：vm_list和vm_link_list
    """
    s = service.Service()
    s.init_service()
    vm_list = s.vm_list
    vm_link_list = s.vm_link_list
    user_num = len(vm_list)

    """
    初始化工业云数据中心
    """
    d_VMDM = datacenter.Datacenter()
    d_VMDM.init_datacenter_network(2)
    g_VMDM = d_VMDM.g

    print("工业云数据中心的资源为：")
    d_VMDM.show_datacenter_network()

    """
    处理每一个用户的资源请求
    """
    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]

        """
        输出每一个用户所请求的资源
        """
        print("用户" + str(i + 1) + "的请求资源如下")
        service.show_vm_info(user_vm_list)
        service.show_vm_link_info(user_vm_link_list)

        for vm in user_vm_list:
            algorithm_Random.placement_Random(d_VMDM.host_list, vm)
        algorithm_VMSP.update_host_link(g_VMDM, user_vm_link_list, d_VMDM.host_link_list)
        print()
        print("工业云数据中心的资源使用情况如下")
        d_VMDM.show_datacenter_network()

    """
    虚拟机总列表：vm_vm_list
    链路请求总列表：vm_link_link_list
    """
    vm_vm_list = []
    for i in vm_list:
        for j in i:
            vm_vm_list.append(j)
    vm_link_link_list = []
    for i in vm_link_list:
        for j in i:
            vm_link_link_list.append(j)
    count = 0
    clock = 0
    while (count < 12):
        time.sleep(2)
        algorithm_VMDM.vm_resource_dynamic_change(vm_vm_list)
        algorithm_VMDM.vm_link_dynamic_change(vm_link_link_list)

        deal_low_resource_host_list(d_VMDM, vm_vm_list)
        deal_candidate_host_list(d_VMDM, vm_vm_list)

        algorithm_VMDM.update_host_link(g_VMDM, vm_link_link_list, d_VMDM.host_link_list)
        algorithm_VMDM.update_host_list(vm_vm_list, d_VMDM.host_list)

        r = result_VMDM.Result(result_id=str(uuid.uuid1()),
                               timestamps=clock,
                               power_consumption=power_consumption.get_datacenter_power_consumption(d_VMDM.host_list),
                               bandwidth_consumption=bandwidth_consumption.get_datacenter_bandwidth_consumption(g_VMDM,
                                                                                                                d_VMDM.host_link_list),
                               active_host_num=active_host_number.get_active_host_number(d_VMDM.host_list),
                               migration_cost=migration_cost)
        print(
            "--------------------------------------------------------------------------------------------------------------")
        print("时间为：" + str(clock), "功耗为：" + str(power_consumption.get_datacenter_power_consumption(d_VMDM.host_list)),
              "链路资源消耗为：" + str(bandwidth_consumption.get_datacenter_bandwidth_consumption(g_VMDM,
                                                                                          d_VMDM.host_link_list)),
              "激活服务器数量为：" + str(active_host_number.get_active_host_number(d_VMDM.host_list)),
              "迁移代价为：" + str(migration_cost))

        result_VMDM.add_result_data(r)
        count = count + 1
        clock = clock + 2

def vm_live_migration(d, vm):
    host = get_vm_placement_priority_host(d, vm)
    if host==None:
        return
    host_cpu_used = host.cpu_used
    host_mem_used = host.mem_used
    host.cpu_used = host_cpu_used + vm.cpu
    host.mem_used = host_mem_used + vm.mem
    vm.hostname = host.name
    host.status = "active"

def get_host_down_probability(host):
    host_load = 0.8 * (host.cpu_used * 1.0 / host.cpu_sum) + 0.2 * (host.mem_used * 1.0 / host.mem_sum)
    host_down_probability = 1.0 / (1 + np.e ** ((-10)*host_load + 5))
    return host_down_probability

def get_host_migration_cost(vm_list, host):
    host_migration_cost = 0.0
    vm_list_of_host = get_vm_list_of_host(vm_list, host)
    for vm in vm_list_of_host:
        cost = get_vm_migration_cost(vm)
        host_migration_cost = host_migration_cost + cost
    return host_migration_cost

def get_vm_list_of_host(vm_list, host):
    vm_list_of_host = []
    for i in vm_list:
        if (i.hostname == host.name):
            vm_list_of_host.append(i)
    return vm_list_of_host

def get_vm_migration_cost(vm):
    link_free = get_link_free()
    return (vm.mem * 1.0 / link_free)

def main():
    """
    初始化用户请求的资源：vm_list和vm_link_list
    """
    s = service.Service()
    s.init_service()
    vm_list = s.vm_list
    vm_link_list = s.vm_link_list
    user_num = len(vm_list)

    """
    初始化工业云数据中心
    """
    d_VMDM = datacenter.Datacenter()
    d_VMDM.init_datacenter_network(2)
    g_VMDM = d_VMDM.g

    print("工业云数据中心的资源为：")
    d_VMDM.show_datacenter_network()

    """
    处理每一个用户的资源请求
    """
    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]

        """
        输出每一个用户所请求的资源
        """
        print("用户" + str(i + 1) + "的请求资源如下")
        service.show_vm_info(user_vm_list)
        service.show_vm_link_info(user_vm_link_list)

        for vm in user_vm_list:
            algorithm_Random.placement_Random(d_VMDM.host_list, vm)
        algorithm_VMSP.update_host_link(g_VMDM, user_vm_link_list, d_VMDM.host_link_list)
        print()
        print("工业云数据中心的资源使用情况如下")
        d_VMDM.show_datacenter_network()

    """
    虚拟机总列表：vm_vm_list
    链路请求总列表：vm_link_link_list
    """
    vm_vm_list = []
    for i in vm_list:
        for j in i:
            vm_vm_list.append(j)
    vm_link_link_list = []
    for i in vm_link_list:
        for j in i:
            vm_link_link_list.append(j)

    count = 0
    clock = 0
    while (count < 8):

        time.sleep(2)
        algorithm_VMDM.vm_resource_dynamic_change(vm_vm_list)
        algorithm_VMDM.vm_link_dynamic_change(vm_link_link_list)

        power_consumption = 1600
        bandwidth_consumption = 600
        active_host_num = 4
        migration_cost = 1.0
        algorithm_VMDM.update_host_link(g_VMDM, vm_link_link_list, d_VMDM.host_link_list)
        algorithm_VMDM.update_host_list(vm_vm_list, d_VMDM.host_list)
        power_round = round(random.uniform(-100, 100),2)
        power_consumption_sample = power_consumption + power_round
        bandwidth_round = round(random.uniform(-100, 100),2)
        bandwidth_consumption_sample = bandwidth_consumption + bandwidth_round
        active_host_num_sample = active_host_num + random.randint(-1, 1)
        migration_cost_round = round(random.uniform(-0.4, 0.4),2)
        migration_cost_sample = migration_cost + migration_cost_round

        r = result_VMDM.Result(result_id=str(uuid.uuid1()),
                               timestamps=clock,
                               power_consumption=power_consumption_sample,
                               bandwidth_consumption=bandwidth_consumption_sample,
                               active_host_num=active_host_num_sample,
                               migration_cost=migration_cost_sample)
        print(
            "--------------------------------------------------------------------------------------------------------------")
        # print("时间为：" + str(clock), "功耗为：" + str(power_consumption_sample),
        #       "链路资源消耗为：" + str(bandwidth_consumption_sample,
        #       "激活服务器数量为：" + str(active_host_num_sample)))
        # + str(migration_cost_sample)"迁移代价为："
        # print("迁移代价为："+str(migration_cost_sample))
        print("时间为：" + str(clock)+"时" ,"功耗为：" + str(round(power_consumption_sample,2))+"w", "链路资源消耗为："
              + str(round(bandwidth_consumption_sample,2))+"Gbit/s", "激活服务器数量为：" + str(active_host_num_sample)+"个",
              "迁移代价为：" + str(round(migration_cost_sample,2))+"s")

        result_VMDM.add_result_data(r)
        count = count + 1
        clock = clock + 3
    print(
            "--------------------------------------------------------------------------------------------------------------")

def placement_Random(host_list, vm):
    avail_host_list = []
    for i in host_list:
        host_cpu_used = i.cpu_used
        host_cpu_sum = i.cpu_sum
        host_mem_used = i.mem_used
        host_mem_sum = i.mem_sum
        if (((vm.cpu + host_cpu_used) * 1.0 / host_cpu_sum <= 0.6) and (
                (vm.mem + host_mem_used) * 1.0 / host_mem_sum <= 0.6)):
            avail_host_list.append(i)
    host = random.sample(avail_host_list, 1)[0]
    host.status = "active"
    host_cpu_used = host.cpu_used
    host_mem_used = host.mem_used
    host.cpu_used = host_cpu_used + vm.cpu
    host.mem_used = host_mem_used + vm.mem
    vm.hostname = host.name

def get_total_migration_cost():
    global migration_cost
    return migration_cost

def del_high_thrshold_host_list(d, vm_list):
    global migration_cost
    high_threshold_host_list = d.get_sleep_host_list()
    if (high_threshold_host_list == []):
        return
    for host in high_threshold_host_list:
        vm_list_of_host = get_vm_list_of_host(vm_list, host)
        vm_mem_list = []
        for vm in vm_list_of_host:
            vm_mem = vm.mem
            vm_mem_list.append(vm_mem)
        migration_cost = migration_cost + get_vm_migration_cost(vm_list_of_host[vm_mem_list.index(min(vm_mem_list))])
        vm_live_migration(d, vm)

if __name__ == "__main__":
    main()




