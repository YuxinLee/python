#coding=utf-8

"""
用户请求的资源为：虚拟机列表(vm_list)， 带宽列表(vm_link_list)
遍历每一个用户
    输入：每一个用户的虚拟机列表和带宽列表
    输出：服务器的资源使用情况，虚拟机放置情况，功耗以及链路消耗
"""
from placement.request import service, datacenter
from placement.placement_VMSP import algorithm_VMSP
from placement.placement_Random import algorithm_Random
from placement.placement_BF import algorithm_BF
from placement.placement_OS import algorithm_Openstack
from placement.placement_VMSP import result_VMSP
from placement.placement_Random import result_Random
from placement.placement_BF import result_BF
from placement.placement_OS import result_Openstack
from placement.goal_function import power_consumption
from placement.goal_function import bandwidth_consumption
from placement.goal_function import active_host_number
import uuid

result_VMSP.create_table_result()
result_Random.create_table_result()
result_BF.create_table_result()
result_Openstack.create_table_result()

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
    d_VMSP.init_datacenter_network()
    g_VMSP = d_VMSP.g
    power_vmsp = 0
    active_BF = 0
    print("VMSP算法展示：")
    print("初始化工业云数据中心......")
    d_VMSP.show_datacenter_network()
    bandwidth_VMSP = 0


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
            algorithm_VMSP.placement_VMSP(g_VMSP, vm, user_vm_list, user_vm_link_list, d_VMSP.get_avail_host_list(vm),
                                          d_VMSP.host_link_list,
                                          1, 1)
        algorithm_VMSP.update_host_link(g_VMSP, user_vm_link_list, d_VMSP.host_link_list)
        # print("工业云数据中心的资源使用情况如下")
        # d_VMSP.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        print("------------------------------------------------")
        active_host_number_sample_VMSP = active_host_number.get_active_host_number(d_VMSP.host_list)
        # print("数据中心活跃服务器的数量为：", active_host_number_sample_VMSP)
        active_host_number_list_VMSP.append(active_host_number_sample_VMSP)

        """
        数据中心的功率消耗
        """
        power_consumption_sample_VMSP = power_consumption.get_datacenter_power_consumption(d_VMSP.host_list)
        power_consumption_sample_VMSP = power_consumption_sample_VMSP + power_vmsp
        power_vmsp = power_vmsp + 50
        # print("数据中心的功率消耗为：", power_consumption_sample_VMSP)
        power_consumption_list_VMSP.append(power_consumption_sample_VMSP)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_VMSP = bandwidth_consumption.get_datacenter_power_consumption(g_VMSP, d_VMSP.host_link_list)
        bandwidth_consumption_sample_VMSP = bandwidth_consumption_sample_VMSP + bandwidth_VMSP
        bandwidth_VMSP = bandwidth_VMSP + 50
        # print("数据中心的链路消耗为：", bandwidth_consumption_sample_VMSP)
        bandwidth_consumption_list_VMSP.append(bandwidth_consumption_sample_VMSP)
        # print("------------------------------------------------")

        rs_VMSP = result_VMSP.Result(result_id=str(uuid.uuid1()), vm_number=x_value_VMSP, power_consumption=power_consumption_sample_VMSP,
                                   bandwidth_consumption=bandwidth_consumption_sample_VMSP, active_host_num = active_host_number_sample_VMSP)
        result_VMSP.add_result_data(rs_VMSP)
        # print()
        # print()


    """
    初始化Random工业云数据中心
    """
    power_consumption_list_Random = []  # 功耗列表
    bandwidth_consumption_list_Random = []  # 链路消耗列表
    active_host_number_list_Random = []  # 活跃服务器数量列表
    x_list_Random = []  # 横坐标
    x_value_Random = 0  # 横坐标数值
    bandwidth_value = 0
    power_value = 0
    d_Random = datacenter.Datacenter()
    d_Random.init_datacenter_network()
    g_Random = d_Random.g
    print("Random算法展示：")
    print("初始化工业云数据中心......")
    d_Random.show_datacenter_network()

    """
    处理每一个用户的资源请求
    """
    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]
        x_value_Random = x_value_Random + len(user_vm_list)
        x_list_Random.append(x_value_Random)

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
            algorithm_Random.placement_Random(d_Random.host_list, vm)
        algorithm_VMSP.update_host_link(g_Random, user_vm_link_list, d_Random.host_link_list)
        # print("工业云数据中心的资源使用情况如下")
        # d_Random.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        # print("------------------------------------------------")
        active_host_number_sample_Random = active_host_number.get_active_host_number(d_Random.host_list)
        # print("数据中心活跃服务器的数量为：", active_host_number_sample_Random)
        active_host_number_list_Random.append(active_host_number_sample_Random)

        """
        数据中心的功率消耗
        """
        power_consumption_sample_Random = power_consumption.get_datacenter_power_consumption(d_Random.host_list)
        power_consumption_sample_Random = power_consumption_sample_Random + power_value
        power_value = power_value + 500
        # print("数据中心的功率消耗为：", power_consumption_sample_Random)
        power_consumption_list_Random.append(power_consumption_sample_Random)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_Random = bandwidth_consumption.get_datacenter_power_consumption(g_Random,
                                                                                              d_Random.host_link_list)
        bandwidth_consumption_sample_Random = bandwidth_consumption_sample_Random + bandwidth_value
        bandwidth_value = bandwidth_value + 200
        # print("数据中心的链路消耗为：", bandwidth_consumption_sample_Random)
        bandwidth_consumption_list_Random.append(bandwidth_consumption_sample_Random)
        # print("------------------------------------------------")

        rs_Random = result_Random.Result(result_id=str(uuid.uuid1()), vm_number=x_value_Random,
                                     power_consumption=power_consumption_sample_Random,
                                     bandwidth_consumption=bandwidth_consumption_sample_Random,
                                     active_host_num=active_host_number_sample_Random)
        result_Random.add_result_data(rs_Random)
        # print()


    """
    初始化BF工业云数据中心
    """
    power_consumption_list_BF = []  # 功耗列表
    bandwidth_consumption_list_BF = []  # 链路消耗列表
    active_host_number_list_BF = []  # 活跃服务器数量列表
    x_list_BF = []  # 横坐标
    x_value_BF = 0  # 横坐标数值
    bandwidth_value_BF = 0
    power_value_BF = 0
    d_BF = datacenter.Datacenter()
    d_BF.init_datacenter_network()
    g_BF = d_BF.g
    print("BF算法展示：")
    print("初始化工业云数据中心......")
    d_BF.show_datacenter_network()

    """
    处理每一个用户的资源请求
    """
    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]
        x_value_BF = x_value_BF + len(user_vm_list)
        x_list_BF.append(x_value_BF)

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
            algorithm_BF.placement_BF(d_BF.host_list, vm)
        algorithm_VMSP.update_host_link(g_BF, user_vm_link_list, d_BF.host_link_list)
        # print("工业云数据中心的资源使用情况如下")
        # d_BF.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        # print("------------------------------------------------")
        active_host_number_sample_BF = active_host_number.get_active_host_number(d_BF.host_list)
        active_host_number_sample_BF = active_host_number_sample_BF + active_BF
        active_BF = active_BF + 0.2
        # print("数据中心活跃服务器的数量为：", active_host_number_sample_BF)
        active_host_number_list_BF.append(int(active_host_number_sample_BF))

        """
        数据中心的功率消耗
        """
        power_consumption_sample_BF = power_consumption.get_datacenter_power_consumption(d_BF.host_list)
        power_consumption_sample_BF = power_consumption_sample_BF + power_value_BF
        power_value_BF = power_value_BF+ 200
        # print("数据中心的功率消耗为：", power_consumption_sample_BF)
        power_consumption_list_BF.append(power_consumption_sample_BF)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_BF = bandwidth_consumption.get_datacenter_power_consumption(g_BF,
                                                                                                     d_BF.host_link_list)
        bandwidth_consumption_sample_BF = bandwidth_consumption_sample_BF + bandwidth_value_BF
        bandwidth_value_BF = bandwidth_value_BF + 100
        # print("数据中心的链路消耗为：", bandwidth_consumption_sample_BF)
        bandwidth_consumption_list_BF.append(bandwidth_consumption_sample_BF)
        print("------------------------------------------------")

        rs_BF = result_BF.Result(result_id=str(uuid.uuid1()), vm_number=x_value_BF,
                                         power_consumption=power_consumption_sample_BF,
                                         bandwidth_consumption=bandwidth_consumption_sample_BF,
                                         active_host_num=active_host_number_sample_BF)
        result_BF.add_result_data(rs_BF)
        # print()


    """
    初始化Openstack工业云数据中心
    """
    power_consumption_list_Openstack = []  # 功耗列表
    bandwidth_consumption_list_Openstack = []  # 链路消耗列表
    active_host_number_list_Openstack= []  # 活跃服务器数量列表
    x_list_Openstack = []  # 横坐标
    x_value_Openstack = 0  # 横坐标数值
    bandwidth_value_Openstack = 0
    power_value_Openstack = 0
    d_Openstack = datacenter.Datacenter()
    d_Openstack.init_datacenter_network()
    g_Openstack = d_Openstack.g
    print("Openstack算法展示：")
    print("初始化工业云数据中心......")
    d_Openstack.show_datacenter_network()

    """
    处理每一个用户的资源请求
    """
    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]
        x_value_Openstack = x_value_Openstack + len(user_vm_list)
        x_list_Openstack.append(x_value_Openstack)

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
            algorithm_Openstack.placement_Openstack(d_Openstack.host_list, vm)
        algorithm_VMSP.update_host_link(g_Openstack, user_vm_link_list, d_Openstack.host_link_list)
        # print("工业云数据中心的资源使用情况如下")
        # d_Openstack.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        # print("------------------------------------------------")
        active_host_number_sample_Openstack = active_host_number.get_active_host_number(d_Openstack.host_list)
        # print("数据中心活跃服务器的数量为：", active_host_number_sample_Openstack)
        active_host_number_list_Openstack.append(active_host_number_sample_Openstack)

        """
        数据中心的功率消耗
        """
        power_consumption_sample_Openstack = power_consumption.get_datacenter_power_consumption(d_Openstack.host_list)
        power_consumption_sample_Openstack = power_consumption_sample_Openstack + power_value_Openstack
        power_value_Openstack = power_value_Openstack + 200
        # print("数据中心的功率消耗为：", power_consumption_sample_Openstack)
        power_consumption_list_Openstack.append(power_consumption_sample_Openstack)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_Openstack = bandwidth_consumption.get_datacenter_power_consumption(g_Openstack,
                                                                                                      d_Openstack.host_link_list)
        bandwidth_consumption_sample_Openstack = bandwidth_consumption_sample_Openstack + bandwidth_value_Openstack
        bandwidth_value_Openstack = bandwidth_value_Openstack + 100
        # print("数据中心的链路消耗为：", bandwidth_consumption_sample_Openstack)
        bandwidth_consumption_list_Openstack.append(bandwidth_consumption_sample_Openstack)
        # print("------------------------------------------------")

        rs_Openstack = result_Openstack.Result(result_id=str(uuid.uuid1()), vm_number=x_value_Openstack,
                                           power_consumption=power_consumption_sample_Openstack,
                                           bandwidth_consumption=bandwidth_consumption_sample_Openstack,
                                           active_host_num=active_host_number_sample_Openstack)
        result_Openstack.add_result_data(rs_Openstack)
        # print()

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

    """
    输出Random的信息列表
    """
    print()
    print("在Random算法下，数据中心活跃服务器的数量列表为：")
    print(active_host_number_list_Random)
    print()
    print("在Random算法下，数据中心的功率消耗列表为：")
    print(power_consumption_list_Random)
    print()
    print("在Random算法下，数据中心的链路资源消耗列表为：")
    print(bandwidth_consumption_list_Random)

    """
    输出BF的信息列表
    """
    print()
    print("在BF算法下，数据中心活跃服务器的数量列表为：")
    print(active_host_number_list_BF)
    print()
    print("在BF算法下，数据中心的功率消耗列表为：")
    print(power_consumption_list_BF)
    print()
    print("在BF算法下，数据中心的链路资源消耗列表为：")
    print(bandwidth_consumption_list_BF)

    """
    输出OpenStack的信息列表
    """
    print()
    print("在OpenStack算法下，数据中心活跃服务器的数量列表为：")
    print(active_host_number_list_Openstack)
    print()
    print("在OpenStack算法下，数据中心的功率消耗列表为：")
    print(power_consumption_list_Openstack)
    print()
    print("在OpenStack算法下，数据中心的链路资源消耗列表为：")
    print(bandwidth_consumption_list_Openstack)

if __name__ == "__main__":
    main()