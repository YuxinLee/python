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
from migration.goal_function import power_consumption
from migration.goal_function import bandwidth_consumption
from migration.goal_function import active_host_number
from migration.goal_function import migration_cost
from migration.migration_VMDM import result_VMDM
from migration.migration_VMDM import algorithm_VMDM
import time
import uuid

result_VMDM.create_table_result()

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
    初始化VMSP工业云数据中心
    """
    power_consumption_list_VMSP = []     #功耗列表
    bandwidth_consumption_list_VMSP = []      #链路消耗列表
    active_host_number_list_VMSP = []                    #活跃服务器数量列表
    x_list_VMSP = []                                     #横坐标
    x_value_VMSP = 0                                    #横坐标数值
    d_VMSP = datacenter.Datacenter()
    d_VMSP.init_datacenter_network(2)
    g_VMSP = d_VMSP.g
    print("利用VMSP算法将虚拟机放置在数据中心：")
    print("初始化工业云数据中心......")
    d_VMSP.show_datacenter_network()

    """
    处理每一个用户的资源请求
    """
    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]
        x_value_VMSP = x_value_VMSP + len(user_vm_list)
        x_list_VMSP.append(x_value_VMSP)

        """
        输出每一个用户所请求的资源
        """
        print("用户" + str(i + 1) + "的请求资源如下")
        service.show_vm_info(user_vm_list)
        service.show_vm_link_info(user_vm_link_list)

        """
        处理用户的每一个虚拟机
        """
        for vm in user_vm_list:
            algorithm_VMSP.placement_VMSP(g_VMSP, vm, user_vm_list, user_vm_link_list, d_VMSP.get_avail_host_list(),
                                          d_VMSP.host_link_list,
                                          1, 1)
        algorithm_VMSP.update_host_link(g_VMSP, user_vm_link_list, d_VMSP.host_link_list)
        print()
        print("工业云数据中心的资源使用情况如下")
        d_VMSP.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        print("------------------------------------------------")
        active_host_number_sample_VMSP = active_host_number.get_active_host_number(d_VMSP.host_list)
        print("数据中心活跃服务器的数量为：", active_host_number_sample_VMSP)
        active_host_number_list_VMSP.append(active_host_number_sample_VMSP)

        """
        数据中心的功率消耗
        """
        power_consumption_sample_VMSP = power_consumption.get_datacenter_power_consumption(d_VMSP.host_list)
        print("数据中心的功率消耗为：", power_consumption_sample_VMSP)
        power_consumption_list_VMSP.append(power_consumption_sample_VMSP)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_VMSP = bandwidth_consumption.get_datacenter_bandwidth_consumption(g_VMSP, d_VMSP.host_link_list)
        print("数据中心的链路消耗为：", bandwidth_consumption_sample_VMSP)
        bandwidth_consumption_list_VMSP.append(bandwidth_consumption_sample_VMSP)
        print("------------------------------------------------")


        print()
        print()

    """
    输出VMSP的信息列表
    """
    print()
    print("在VMSP算法下，数据中心活跃服务器的数量列表为：")
    print(active_host_number_list_VMSP)
    print()
    print("在VMSP算法下，数据中心的功率消耗列表为：")
    print(power_consumption_list_VMSP)
    print()
    print("在VMSP算法下，数据中心的链路资源消耗列表为：")
    print(bandwidth_consumption_list_VMSP)
    print()

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

    # for i in vm_vm_list:
    #     print(i.name)
    # for i in vm_link_link_list:
    #     print(i.name)



    g_VMDM = g_VMSP
    d_VMDM = d_VMSP

    count = 0
    clock = 0
    while (count < 12):
        time.sleep(2)
        algorithm_VMDM.vm_resource_dynamic_change(vm_vm_list)
        algorithm_VMDM.vm_link_dynamic_change(vm_link_link_list)
        # algorithm_VMDM.del_low_resource_host(g_VMDM, d_VMDM, d_VMDM.get_low_resource_host_list(), vm_vm_list, vm_link_link_list,
        #                                       d_VMDM.host_link_list, 1, 1)
        #
        # algorithm_VMDM.del_candidate_host(g_VMDM, d_VMDM, vm_vm_list, vm_link_link_list,
        #                                   d_VMDM.host_link_list, 1, 1, d_VMDM.get_candidate_host_list())
        algorithm_VMDM.update_host_link(g_VMDM, vm_link_link_list, d_VMDM.host_link_list)
        algorithm_VMDM.update_host_list(vm_vm_list, d_VMDM.host_list)

        r = result_VMDM.Result(result_id=str(uuid.uuid1()),
                                               timestamps=clock,
                                               power_consumption=power_consumption.get_datacenter_power_consumption(d_VMDM.host_list),
                                               bandwidth_consumption=bandwidth_consumption.get_datacenter_bandwidth_consumption(g_VMDM,
                                                                                                      d_VMDM.host_link_list),
                                               active_host_num=active_host_number.get_active_host_number(d_VMDM.host_list),
                                               migration_cost=migration_cost.get_migration_cost())
        print("--------------------------------------------------------------------------------------------------------------")
        print("时间为："+str(clock), "功耗为："+str(power_consumption.get_datacenter_power_consumption(d_VMDM.host_list)),
              "链路资源消耗为："+str(bandwidth_consumption.get_datacenter_bandwidth_consumption(g_VMDM,
                                                                                                      d_VMDM.host_link_list)),
              "激活服务器数量为："+str(active_host_number.get_active_host_number(d_VMDM.host_list)),
              "迁移代价为："+str(migration_cost.get_migration_cost()))

        result_VMDM.add_result_data(r)
        count = count + 1
        clock = clock + 2

if __name__ == "__main__":
    main()