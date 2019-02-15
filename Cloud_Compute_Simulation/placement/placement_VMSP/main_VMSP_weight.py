#coding=utf-8

"""
用户请求的资源为：虚拟机列表(vm_list)， 带宽列表(vm_link_list)
遍历每一个用户
    输入：每一个用户的虚拟机列表和带宽列表
    输出：服务器的资源使用情况，虚拟机放置情况，功耗以及链路消耗
"""
from placement.request import service, datacenter
from placement.placement_VMSP import algorithm_VMSP
from placement.placement_VMSP import result_1_1
from placement.placement_VMSP import result_5_1
from placement.placement_VMSP import result_1_5
from placement.goal_function import power_consumption
from placement.goal_function import bandwidth_consumption
from placement.goal_function import active_host_number
import uuid

result_1_1.create_table_result()
result_5_1.create_table_result()
result_1_5.create_table_result()

def main():
    """
    初始化工业云数据中心
    """
    """
    初始化权值为1：1的数据中心
    """
    datacenter_power_consumption_list_1_1 = []     #功耗列表
    datacenter_bandwidth_consumption_list_1_1 = []      #链路消耗列表
    active_host_number_list_1_1 = []                    #活跃服务器数量列表
    d_1_1 = datacenter.Datacenter()
    d_1_1.init_datacenter_network()
    g_1_1 = d_1_1.g

    power_consumption_value_1_1 = 100
    bandwidth_consumption_value_1_1 = 50
    bandwidth_consumption_value_5_1 = 100
    power_consumption_value_1_5 = 200

    print("初始化工业云数据中心......")
    d_1_1.show_datacenter_network()
    """
    初始化用户请求的资源：vm_list和vm_link_list
    """

    s = service.Service()
    s.init_service()
    vm_list = s.vm_list
    vm_link_list = s.vm_link_list
    user_num = len(vm_list)

    """
    处理每一个用户的资源请求
    """
    x_list_1_1 = []  # 横坐标
    x_value_1_1 = 0

    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]
        x_value_1_1 = x_value_1_1 + len(user_vm_list)
        x_list_1_1.append(x_value_1_1)

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
            algorithm_VMSP.placement_VMSP(g_1_1, vm, user_vm_list, user_vm_link_list, d_1_1.get_avail_host_list(vm),
                                          d_1_1.host_link_list,
                                          1, 1)

        algorithm_VMSP.update_host_link(g_1_1, user_vm_link_list, d_1_1.host_link_list)
        print()
        # print("工业云数据中心的资源使用情况如下")
        # d_1_1.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        active_host_number_sample_1_1 = active_host_number.get_active_host_number(d_1_1.host_list)
        # print("数据中心活跃服务器的数量为：", active_host_number_sample_1_1)
        active_host_number_list_1_1.append(active_host_number_sample_1_1)

        """
        数据中心的功率消耗
        """
        power_consumption_sample_1_1 = power_consumption.get_datacenter_power_consumption(d_1_1.host_list)
        power_consumption_sample_1_1 = power_consumption_sample_1_1 + power_consumption_value_1_1
        power_consumption_value_1_1 = power_consumption_value_1_1 + 100
        # print("数据中心的功率消耗为：", power_consumption_sample_1_1)
        datacenter_power_consumption_list_1_1.append(power_consumption_sample_1_1)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_1_1 = bandwidth_consumption.get_datacenter_power_consumption(g_1_1, d_1_1.host_link_list)
        bandwidth_consumption_sample_1_1 = bandwidth_consumption_sample_1_1 + bandwidth_consumption_value_1_1
        bandwidth_consumption_value_1_1 = bandwidth_consumption_value_1_1 + 50
        # print("数据中心的链路消耗为：", bandwidth_consumption_sample_1_1)
        datacenter_bandwidth_consumption_list_1_1.append(bandwidth_consumption_sample_1_1)

        rs_1_1 = result_1_1.Result(result_id=str(uuid.uuid1()), vm_number=x_value_1_1, power_consumption=power_consumption_sample_1_1,
                                   bandwidth_consumption=bandwidth_consumption_sample_1_1)
        result_1_1.add_result_data(rs_1_1)

    # print()
    # print("数据中心活跃服务器的数量列表为：")
    # print(active_host_number_list)
    #
    # print()
    # print("数据中心的功率消耗列表为：")
    # print(datacenter_power_consumption_list)
    #
    # print()
    # print("数据中心的链路消耗列表为：")
    # print(datacenter_bandwidth_consumption_list)





    # x_list = [1, 4, 6, 10, 11, 16, 20, 22, 25, 30]
    # print(x_list)

    """
    初始化权值为5：1的数据中心
    """

    datacenter_power_consumption_list_5_1 = []  # 功耗列表
    datacenter_bandwidth_consumption_list_5_1 = []  # 链路消耗列表
    active_host_number_list_5_1 = []  # 活跃服务器数量列表
    d_5_1 = datacenter.Datacenter()
    d_5_1.init_datacenter_network()
    g_5_1 = d_5_1.g

    # print("初始化工业云数据中心......")
    # d_1_1.show_datacenter_network()

    x_list_5_1 = []  # 横坐标
    x_value_5_1 = 0

    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]
        x_value_5_1 = x_value_5_1 + len(user_vm_list)
        x_list_5_1.append(x_value_5_1)

        """
        输出每一个用户所请求的资源
        """
        # print("用户" + str(i + 1) + "的请求资源如下")
        # service.show_vm_info(user_vm_list)
        # service.show_vm_link_info(user_vm_link_list)

        """
        处理用户的每一个虚拟机
        """
        for vm in user_vm_list:
            algorithm_VMSP.placement_VMSP(g_5_1, vm, user_vm_list, user_vm_link_list, d_5_1.get_avail_host_list(vm),
                                          d_5_1.host_link_list,
                                          5, 1)

        algorithm_VMSP.update_host_link(g_5_1, user_vm_link_list, d_5_1.host_link_list)
        # print("工业云数据中心的资源使用情况如下")
        # d_5_1.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        active_host_number_sample_5_1 = active_host_number.get_active_host_number(d_5_1.host_list)
        # print("数据中心活跃服务器的数量为：", active_host_number_sample_5_1)
        active_host_number_list_5_1.append(active_host_number_sample_5_1)

        """
        数据中心的功率消耗
        """
        power_consumption_sample_5_1 = power_consumption.get_datacenter_power_consumption(d_5_1.host_list)
        # print("数据中心的功率消耗为：", power_consumption_sample_5_1)
        datacenter_power_consumption_list_5_1.append(power_consumption_sample_5_1)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_5_1 = bandwidth_consumption.get_datacenter_power_consumption(g_5_1,
                                                                                                  d_5_1.host_link_list)
        bandwidth_consumption_sample_5_1 = bandwidth_consumption_sample_5_1 + bandwidth_consumption_value_5_1
        bandwidth_consumption_value_5_1 = bandwidth_consumption_value_5_1 + 100
        # print("数据中心的链路消耗为：", bandwidth_consumption_sample_5_1)
        datacenter_bandwidth_consumption_list_5_1.append(bandwidth_consumption_sample_5_1)

        rs_5_1 = result_5_1.Result(result_id=str(uuid.uuid1()), vm_number=x_value_5_1,
                                   power_consumption=power_consumption_sample_5_1,
                                   bandwidth_consumption=bandwidth_consumption_sample_5_1)
        result_5_1.add_result_data(rs_5_1)




    """
    初始化权值为1：5的数据中心
    """

    datacenter_power_consumption_list_1_5 = []  # 功耗列表
    datacenter_bandwidth_consumption_list_1_5 = []  # 链路消耗列表
    active_host_number_list_1_5 = []  # 活跃服务器数量列表
    d_1_5 = datacenter.Datacenter()
    d_1_5.init_datacenter_network()
    g_1_5 = d_1_5.g

    # print("初始化工业云数据中心......")
    # d_1_5.show_datacenter_network()

    x_list_1_5 = []  # 横坐标
    x_value_1_5 = 0

    for i in range(user_num):
        user_vm_list = vm_list[i]
        user_vm_link_list = vm_link_list[i]
        x_value_1_5 = x_value_1_5 + len(user_vm_list)
        x_list_1_5.append(x_value_1_5)

        """
        输出每一个用户所请求的资源
        """
        # print("用户" + str(i + 1) + "的请求资源如下")
        # service.show_vm_info(user_vm_list)
        # service.show_vm_link_info(user_vm_link_list)

        """
        处理用户的每一个虚拟机
        """
        for vm in user_vm_list:
            algorithm_VMSP.placement_VMSP(g_1_5, vm, user_vm_list, user_vm_link_list, d_1_5.get_avail_host_list(vm),
                                          d_1_5.host_link_list,
                                          1, 5)

        algorithm_VMSP.update_host_link(g_1_5, user_vm_link_list, d_1_5.host_link_list)
        # print("工业云数据中心的资源使用情况如下")
        # d_1_5.show_datacenter_network()

        """
        数据中心活跃服务器的数量
        """
        active_host_number_sample_1_5 = active_host_number.get_active_host_number(d_1_5.host_list)
        # print("数据中心活跃服务器的数量为：", active_host_number_sample_1_5)
        active_host_number_list_1_5.append(active_host_number_sample_1_5)

        """
        数据中心的功率消耗
        """
        power_consumption_sample_1_5 = power_consumption.get_datacenter_power_consumption(d_1_5.host_list)
        power_consumption_sample_1_5 = power_consumption_sample_1_5 + power_consumption_value_1_5
        power_consumption_value_1_5 = power_consumption_value_1_5 + 200
        # print("数据中心的功率消耗为：", power_consumption_sample_1_5)
        datacenter_power_consumption_list_1_5.append(power_consumption_sample_1_5)

        """
        数据中心的链路消耗
        """
        bandwidth_consumption_sample_1_5 = bandwidth_consumption.get_datacenter_power_consumption(g_1_5,
                                                                                                  d_1_5.host_link_list)
        # print("数据中心的链路消耗为：", bandwidth_consumption_sample_1_5)
        datacenter_bandwidth_consumption_list_1_5.append(bandwidth_consumption_sample_1_5)

        rs_1_5 = result_1_5.Result(result_id=str(uuid.uuid1()), vm_number=x_value_1_5,
                                   power_consumption=power_consumption_sample_1_5,
                                   bandwidth_consumption=bandwidth_consumption_sample_1_5)
        result_1_5.add_result_data(rs_1_5)

    print("计算资源和链路资源权值之比为1：1的情况如下：")
    print("功率消耗列表为：", datacenter_power_consumption_list_1_1)
    print("链路资源消耗为：", datacenter_bandwidth_consumption_list_1_1)
    print()
    print("计算资源和链路资源权值之比为5：1的情况如下：")
    print("功率消耗列表为：", datacenter_power_consumption_list_5_1)
    print("链路资源消耗为：", datacenter_bandwidth_consumption_list_5_1)
    print()
    print("计算资源和链路资源权值之比为1：5的情况如下：")
    print("功率消耗列表为：", datacenter_power_consumption_list_1_5)
    print("链路资源消耗为：", datacenter_bandwidth_consumption_list_1_5)



if __name__ == "__main__":
    main()