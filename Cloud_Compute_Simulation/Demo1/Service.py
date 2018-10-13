#coding=utf-8

from Demo1 import DataCenter
from Demo1 import Vm
from Demo1 import Algorithm
from Demo1 import show
from Demo1 import Energy_Consumption
from Demo1 import Bandwidth_Consumption

#初始化数据中心
DataCenter.init_datacenter()
host_list = DataCenter.get_host_list()
vm_vm_bandwidth = dict()
vm_list = []

if __name__ == "__main__":

    while(True):
        number = int(input("请用户输入申请实例的数量：(1-1000)"))
        #print(type(number))

        if(number<1):
            print("您输入有误！请重新输入！")
        elif(number==1):
            print ("请输入您的配置需求：实例名称，CPU资源，内存资源，磁盘空间")
            vm_name = input("实例名称：")
            vm_cpu = int(input("CPU资源(单位：核数)："))
            vm_mem = int(input("内存资源(单位：MB)："))
            vm_disk = int(input("磁盘空间(单位：GB)："))

            vm = Vm.Vm(vm_name, vm_cpu, vm_mem, vm_disk)

            vm_list.append(vm)

            #使用单机模式的算法(cpu和内存阈值为0.8，遍历可用主机，计算最大资源平衡度，然后放置在资源平衡度最大的主机上)
            host = Algorithm.get_best_resource_balance_host(vm_cpu, vm_mem)
            vm.set_vm_host(host)
            Algorithm.algorithm_single_vm(vm_cpu, vm_mem, vm_disk)



        else:

            vm_temp_list = []
            for i in range(number):
                print("请输入您的第" + str(i + 1) + "个实例的配置需求：实例名称, CPU资源, 内存资源, 磁盘空间")
                vm_name = input("实例名称：")
                vm_cpu = int(input("CPU资源(单位：核数)："))
                vm_mem = int(input("内存资源(单位：MB)："))
                vm_disk = int(input("磁盘空间(单位：GB)："))

                vm = Vm.Vm(vm_name, vm_cpu, vm_mem, vm_disk)

                #局部虚拟机列表
                vm_temp_list.append(vm)

                #全局虚拟机列表
                vm_list.append(vm)

            bandwidth_list = []
            vm_vm_temp_bandwidth = dict()
            vm_temp_number = len(vm_temp_list)
            for i in range(0, number-1, 1):
                for j in range(i+1, number, 1):
                    bandwidth = int(input(("请输入")+vm_temp_list[i].get_vm_name()+"实例与"+vm_temp_list[j].get_vm_name()+"实例的带宽需求："))
                    vm_vm_temp_bandwidth[vm_temp_list[i].get_vm_name()+":"+vm_temp_list[j].get_vm_name()] = bandwidth
                    vm_vm_bandwidth[vm_temp_list[i].get_vm_name() + ":" + vm_temp_list[j].get_vm_name()] = bandwidth
                    bandwidth_list.append(bandwidth)

            # for key in vm_vm_bandwidth:
            #     print(key + " "+ str(vm_vm_bandwidth[key]))
            vm_temp_list.reverse()
            bandwidth_list.reverse()
            #多机模式的第一个实例遵循单机模式的规则
            v = vm_temp_list[0]
            h = Algorithm.get_best_resource_balance_host(v.get_vm_cpu(), v.get_vm_mem())
            v.set_vm_host(h)
            Algorithm.algorithm_single_vm(v.get_vm_cpu(), v.get_vm_mem(), v.get_vm_disk())

            #第二个实例开始需要遵循多机模式，即在考虑资源平衡度的时候同时要考虑网络带宽
            for i in range(1, vm_temp_number, 1):
                vm = vm_temp_list[i]
                bandwidth_temp_list = bandwidth_list[0:i]

                max_bandwidth = max(bandwidth_temp_list)
                max_bandwidth_index = bandwidth_temp_list.index(max_bandwidth)
                del bandwidth_list[0:i]

                max_resource_balance = Algorithm.get_max_resource_balance(vm.get_vm_cpu(), vm.get_vm_mem())

                if((max_resource_balance * 5000) > max_bandwidth):
                    host = Algorithm.get_best_resource_balance_host(vm.get_vm_cpu(), vm.get_vm_mem())
                    vm.set_vm_host(host)
                    Algorithm.algorithm_single_vm(vm.get_vm_cpu(), vm.get_vm_mem(), vm.get_vm_disk())
                else:
                    host = vm_temp_list[max_bandwidth_index]
                    vm.set_vm_host(host)
                    Algorithm.algorithm_more_vm(vm.get_vm_cpu(), vm.get_vm_mem(), vm.get_vm_disk(), host)

        # 显示主机的资源使用情况
        # show.show_all_host_info(host_list)

        # 显示数据中心的能耗
        g = DataCenter.get_network_graph()
        print("工业云数据中心的能耗为：", Energy_Consumption.get_datacenter_energy_consumption(host_list))
        print("工业云数据中心的带宽消耗为：", Bandwidth_Consumption.get_datacenter_link_bandwidth_consumption(g, vm_vm_bandwidth, vm_list))



