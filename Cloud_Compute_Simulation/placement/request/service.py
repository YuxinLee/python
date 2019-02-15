#coding=utf-8

"""
用户的请求：单机模式和多机模式
单机模式：vm(cpu, mem, disk)
多机模式：vm(cpu, mem, disk) 以及bandwidth
本次实验设置用户数量为10，分别申请（1, 3, 2, 3, 1, 2, 3, 2, 1, 2)
"""

import random
import uuid

"""
定义虚拟机vm：属性分别为：名字，id，cpu，mem，disk，以及放置的服务器
"""
class Vm:
    def __init__(self, name, uuid, cpu, mem, disk, hostname="default"):
        self.name = name
        self.uuid = uuid
        self.cpu = cpu
        self.mem = mem
        self.disk = disk
        self.hostname = hostname

"""
定义虚拟机之间的链路：属性为：名字，id，两个端点，以及带宽
"""
class Vm_Link:
    def __init__(self, name, uuid, vm1, vm2, bandwidth):
        self.name = name
        self.uuid = uuid
        self.vm1 = vm1
        self.vm2 = vm2
        self.bandwidth = bandwidth

"""
定义用户的请求，最后会得到：虚拟机列表以及虚拟机链路列表
"""
class Service:
    def init_service(self):
        vm_value = 1
        vm_link_value = 1
        self.vm_list = []
        self.vm_link_list = []
        request_list = [1, 3, 2, 3, 1, 2, 3, 2, 1, 2]  # 用户请求列表
        flavor_list = [[1,1,1], [1,2,20], [2,4,40], [4,8,80], [8,16,160]]

        # cpu_list = [1, 2, 4, 8, 12]  # cpu请求列表
        # mem_list = [1, 2, 4, 8, 16]  # mem请求列表
        # disk_list = [10, 40, 100, 200, 300]  # disk请求列表
        bandwidth_list = [1, 5, 10, 20, 30]  # 带宽请求列表

        for i in request_list:
            user_vm_num = i         #每个用户的虚拟机数量
            user_vm_list = []
            user_bandwidth_list = []
            for j in range(user_vm_num):         #添加虚拟机
                flavor = random.sample(flavor_list, 1)[0]
                cpu = flavor[0]
                mem = flavor[1]
                disk = flavor[2]
                vm_id = str(uuid.uuid1())
                vm = Vm("Vm" + str(vm_value), vm_id, cpu, mem, disk)
                vm_value = vm_value + 1
                user_vm_list.append(vm)
            self.vm_list.append(user_vm_list)

            for x in range(0, user_vm_num - 1, 1):  # 添加带宽
                for y in range(x + 1, user_vm_num, 1):
                    vm_link_id = str(uuid.uuid1())
                    bandwidth = random.sample(bandwidth_list, 1)[0]
                    vm_link = Vm_Link("vm_link" + str(vm_link_value), vm_link_id, user_vm_list[x], user_vm_list[y],
                                      bandwidth)
                    vm_link_value = vm_link_value + 1
                    user_bandwidth_list.append(vm_link)
            self.vm_link_list.append(user_bandwidth_list)

"""
显示请求的虚拟机信息
"""
def show_vm_info(user_vm_list):
    if (user_vm_list==[]):
        return
    print("虚拟机资源请求为：")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------------")
    for i in user_vm_list:
        print("  虚拟机的名字为：", i.name, "  虚拟机的id为：", i.uuid, "  虚拟机的cpu为：", str(i.cpu)+"核", "  虚拟机的mem为："
              , str(i.mem)+"G", "  虚拟机的disk为", str(i.disk)+"G")
    print(
        "-----------------------------------------------------------------------------------------------------------------------------------------------")
    print()

"""
显示请求的虚拟机链路信息
"""
def show_vm_link_info(user_vm_link_list):
    print("链路资源请求为：")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    if (user_vm_link_list==[]):
        print("没有链路资源请求")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        return
    for i in user_vm_link_list:
        print("  链路的名字为：", i.name, "  链路的id为：", i.uuid, "  链路的端点为：", i.vm1.name+"和"+i.vm2.name, "  链路的带宽为：",
              str(i.bandwidth)+"Gbit/s")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print()


