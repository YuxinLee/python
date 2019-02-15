#coding=utf-8

"""
输入参数
        :param one_or_more:     是否单机模式
        :param servicename:     服务器名字
        :param cpu:             CPU需求
        :param memory:          内存需求
        :param storage:         硬盘需求
        返回值
        :return:                映射结果
"""

def service():
    while (True):
        number = int(input("请用户输入申请服务器的数量：(1-1000)"))

        if (number == 1):
            print("请输入您的配置需求：服务器名称, CPU资源, 内存资源, 磁盘空间")
            service_name = input("服务器名称：")
            service_cpu = int(input("CPU资源(单位：核数)："))
            service_mem = int(input("内存资源(单位：MB)："))
            service_disk = int(input("磁盘空间(单位：GB)："))

            s = Service.Service(service_name, service_cpu, service_mem, service_disk)
            s.algorithm_one_demo()




        elif (number > 1):
            service_list = []

            for i in range(number):
                print("请输入您的第" + str(i + 1) + "台服务器的配置需求：服务器名称, CPU资源, 内存资源, 磁盘空间")
                service_name = input("服务器名称：")
                service_cpu = int(input("CPU资源(单位：核数)："))
                service_mem = int(input("内存资源(单位：MB)："))
                service_disk = int(input("磁盘空间(单位：GB)："))

                service_dict = dict()
                service_dict["service_name"] = service_name
                service_dict["service_cpu"] = service_cpu
                service_dict["service_mem"] = service_mem
                service_dict["service_disk"] = service_disk

                service_list.append(service_dict)

            service_list.reverse()
            # print (service_list)

            # 当申请n台服务器时，这n台服务器之间的链路共有 n*(n-1)/2 条链路
            # count = int((number-1) * number / 2)
            # print ("请输入您的带宽需求：")

            bandwidth_list = [[] for i in range(number - 1)]

            for i in range(0, number - 1, 1):
                for j in range(i + 1, number, 1):
                    # print ("请输入" + service_list[i]['service_name'] + "服务器与" + service_list[j]['service_name'] + "服务器的带宽需求：")
                    bandwidth = int(input("请输入" + service_list[i]['service_name'] + "服务器与" + service_list[j][
                        'service_name'] + "服务器的带宽需求："))
                    # print (i,j)
                    # print (service_list[i]['service_name'] +"---"+ service_list[j]['service_name'])
                    bandwidth_list[i].append(bandwidth)

            for i in range(len(bandwidth_list)):
                bandwidth_list[i].reverse()

            bandwidth_list.reverse()
            # print (bandwidth_list)
            # print ("第一个节点为："+service_list[number-1]['service_name'])

            s = Service.Service(service_list[number - 1]['service_name'], service_list[number - 1]['service_cpu'],
                                service_list[number - 1]['service_mem'], service_list[number - 1]['service_disk'])
            s.algorithm_one_demo()

            service_list.reverse()
            v = Vm_Info.Vm_Info()

            for i in range(1, number, 1):
                s = Service.Service(service_list[i]['service_name'], service_list[i]['service_cpu'],
                                    service_list[i]['service_mem'], service_list[i]['service_disk'])
                max_bandwidth = max(bandwidth_list[i - 1])
                # print (max_bandwidth)
                # s.algorithm_more_demo()
                r = Resource_Balance.Resource_Balance(service_list[i]['service_cpu'], service_list[i]['service_mem'])
                max_resource_balance = r.get_max_resource_balance()
                max_index = bandwidth_list[i - 1].index(max_bandwidth)

                if ((max_resource_balance * 5000) > max_bandwidth):
                    hostname = r.get_best_resource_balance_hostname()
                else:
                    hostname = v.get_hostname_of_vm_name(service_list[max_index]['service_name'])
                # print (service_list[max_index]['service_name'])
                s.algorithm_more_demo(hostname)

            lnk = Link.Link()
            for i in range(len(bandwidth_list)):
                for j in range(len(bandwidth_list[i])):
                    # print (bandwidth_list[i][j])
                    # print (service_list[i+1]['service_name'] + "服务器与" + service_list[j]['service_name'] + "服务器")
                    bandwidth_use = lnk.get_virtual_link_resource(
                        v.get_hostname_of_vm_name(service_list[i + 1]['service_name']),
                        v.get_hostname_of_vm_name(service_list[j]['service_name']), bandwidth_list[i][j])


        else:
            print("您输入有误，请重新输入，谢谢！！！")

        print("消耗的网络带宽的总量为：" + bandwidth_use)

