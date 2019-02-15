#coding=utf-8

"""
数据中心的网络：
                                core_switch_s1                           10000                             core_switch_s2

                        10000                        10000                                        10000                    10000

               access_switch_s3             access_switch_s4                        access_switch_s5             access_switch_s6

            1000            1000            1000            1000                        1000            1000            1000           1000

        compute1 compute2 compute3 |            compute4 compute5/                      compute6 compute7             compute8 compute9


数据中心9台服务器：  CPU核数：32核，内存：64GB，硬盘：2TB， 带宽：1Gbit/s
"""

import networkx as nx
import uuid

"""
定义服务器Host，属性包括：名字，id，cpu总量，mem总量，cpu使用量，mem使用量，服务器的状态(激活与休眠)
"""
class Host:
    def __init__(self, name, uuid, cpu_sum, mem_sum, cpu_used, mem_used, status="sleep"):
        self.name = name
        self.uuid = uuid
        self.cpu_sum = cpu_sum
        self.mem_sum = mem_sum
        self.cpu_used = cpu_used
        self.mem_used = mem_used
        self.status = status

"""
定义物理链路Host_List，属性包括：名字，id，两个端点的名字，bandwidth总量，bandwidth使用量
"""
class Host_Link:
    def __init__(self, name, uuid, node1_name, node2_name, bandwidth_sum, bandwidth_used):
        self.name = name
        self.uuid = uuid
        self.node1_name = node1_name
        self.node2_name = node2_name
        self.bandwidth_sum = bandwidth_sum
        self.bandwidth_used = bandwidth_used

"""
定义数据中心，获取资源Host和Host_Link
"""
class Datacenter:
    def __init__(self):
        self.g = nx.Graph()
        self.g.clear()
        self.g.graph["name"] = "工业云数据中心网络拓扑"

    def init_datacenter_network(self):
        self.g.add_node("core_switch_s1")
        self.g.add_node("core_switch_s2")
        self.g.add_node("access_switch_s3")
        self.g.add_node("access_switch_s4")
        self.g.add_node("access_switch_s5")
        self.g.add_node("access_switch_s6")
        self.g.add_node("compute1")
        self.g.add_node("compute2")
        self.g.add_node("compute3")
        self.g.add_node("compute4")
        self.g.add_node("compute5")
        self.g.add_node("compute6")
        self.g.add_node("compute7")
        self.g.add_node("compute8")
        self.g.add_node("compute9")
        # print(self.g.nodes)

        self.host_list = []
        self.host_link_list = []
        """
        添加服务器节点
        """

        for i in range(1, 10, 1):
            host_name = "compute" + str(i)
            cpu_sum = 32
            mem_sum = 64
            cpu_used = 0
            mem_used = 0
            host = Host(host_name, uuid.uuid1(), cpu_sum , mem_sum, cpu_used, mem_used)
            self.host_list.append(host)

        """
        添加核心交换机与核心交换机的链路 以及 添加核心交换机与接入交换机的链路
        """
        self.g.add_edge("core_switch_s1", "core_switch_s2", bandwidth_sum=10000, bandwidth_used=0)

        self.g.add_edge("core_switch_s1", "access_switch_s3", bandwidth_sum=10000, bandwidth_used=0)
        self.g.add_edge("core_switch_s1", "access_switch_s4", bandwidth_sum=10000, bandwidth_used=0)

        self.g.add_edge("core_switch_s2", "access_switch_s5", bandwidth_sum=10000, bandwidth_used=0)
        self.g.add_edge("core_switch_s2", "access_switch_s6", bandwidth_sum=10000, bandwidth_used=0)

        self.g.add_edge("access_switch_s3", "compute1", bandwidth_sum=1000, bandwidth_used=0)
        self.g.add_edge("access_switch_s3", "compute2", bandwidth_sum=1000, bandwidth_used=0)
        self.g.add_edge("access_switch_s3", "compute3", bandwidth_sum=1000, bandwidth_used=0)

        self.g.add_edge("access_switch_s4", "compute4", bandwidth_sum=1000, bandwidth_used=0)
        self.g.add_edge("access_switch_s4", "compute5", bandwidth_sum=1000, bandwidth_used=0)

        self.g.add_edge("access_switch_s5", "compute6", bandwidth_sum=1000, bandwidth_used=0)
        self.g.add_edge("access_switch_s5", "compute7", bandwidth_sum=1000, bandwidth_used=0)

        self.g.add_edge("access_switch_s6", "compute8", bandwidth_sum=1000, bandwidth_used=0)
        self.g.add_edge("access_switch_s6", "compute9", bandwidth_sum=1000, bandwidth_used=0)

        # print(self.g.edges)

        host_link1 = Host_Link("Host_Link1" , uuid.uuid1(), "core_switch_s1",
                              "core_switch_s2", 10000, 0)
        host_link2 = Host_Link("Host_Link2", uuid.uuid1(), "core_switch_s1",
                               "access_switch_s3", 10000, 0)
        host_link3 = Host_Link("Host_Link3", uuid.uuid1(), "core_switch_s1",
                               "access_switch_s4", 10000, 0)
        host_link4 = Host_Link("Host_Link4", uuid.uuid1(), "core_switch_s2",
                               "access_switch_s5", 10000, 0)
        host_link5 = Host_Link("Host_Link5", uuid.uuid1(), "core_switch_s2",
                               "access_switch_s6", 10000, 0)
        host_link6 = Host_Link("Host_Link6", uuid.uuid1(), "access_switch_s3",
                               "compute1", 1000, 0)
        host_link7 = Host_Link("Host_Link7", uuid.uuid1(), "access_switch_s3",
                               "compute2", 1000, 0)
        host_link8 = Host_Link("Host_Link8", uuid.uuid1(), "access_switch_s3",
                               "compute3", 1000, 0)
        host_link9 = Host_Link("Host_Link9", uuid.uuid1(), "access_switch_s4",
                               "compute4", 1000, 0)
        host_link10 = Host_Link("Host_Link10", uuid.uuid1(), "access_switch_s4",
                               "compute5", 1000, 0)
        host_link11 = Host_Link("Host_Link11", uuid.uuid1(), "access_switch_s5",
                                "compute6", 1000, 0)
        host_link12 = Host_Link("Host_Link12", uuid.uuid1(), "access_switch_s5",
                                "compute7", 1000, 0)
        host_link13 = Host_Link("Host_Link13", uuid.uuid1(), "access_switch_s6",
                                "compute8", 1000, 0)
        host_link14 = Host_Link("Host_Link14", uuid.uuid1(), "access_switch_s6",
                                "compute9", 1000, 0)

        self.host_link_list.append(host_link1)
        self.host_link_list.append(host_link2)
        self.host_link_list.append(host_link3)
        self.host_link_list.append(host_link4)
        self.host_link_list.append(host_link5)
        self.host_link_list.append(host_link6)
        self.host_link_list.append(host_link7)
        self.host_link_list.append(host_link8)
        self.host_link_list.append(host_link9)
        self.host_link_list.append(host_link10)
        self.host_link_list.append(host_link11)
        self.host_link_list.append(host_link12)
        self.host_link_list.append(host_link13)
        self.host_link_list.append(host_link14)

    """
    获取休眠服务器列表
    """
    def get_sleep_host_list(self):
        sleep_host_list = []
        for i in self.host_list:
            if (i.status == "sleep"):
                sleep_host_list.append(i)
        return sleep_host_list

    """
    获取激活服务器列表
    """
    def get_active_host_list(self):
        active_host_list = []
        for i in self.host_list:
            if(i.status == "active"):
                active_host_list.append(i)
        return active_host_list

    """
    过滤：获取符合cpu和mem资源的可用服务器列表
    """
    def get_avail_host_list(self, vm):
        avail_host_list = []
        active_host_list = self.get_active_host_list()
        sleep_host_list = self.get_sleep_host_list()
        if(active_host_list == []):
            host = sleep_host_list[0]
            host.status = "active"
            active_host_list.append(host)
        for i in active_host_list:
            host_cpu_used = i.cpu_used
            host_cpu_sum = i.cpu_sum
            host_mem_used = i.mem_used
            host_mem_sum = i.mem_sum
            if (((vm.cpu + host_cpu_used) * 1.0 / host_cpu_sum <= 0.6) and ((vm.mem + host_mem_used) * 1.0 / host_mem_sum <= 0.6)):
                avail_host_list.append(i)
        if (avail_host_list == []):
            temp_list = self.get_sleep_host_list()
            temp_list[0].status = "active"
            avail_host_list.append(temp_list[0])
        return avail_host_list

    """
    展示数据中心的资源情况，具体包括服务器的资源和物理链路的使用情况
    """
    def show_datacenter_network(self):
        print("服务器资源使用情况为：")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        host_list = self.host_list
        for i in host_list:
            print("  服务器的名字为：", i.name, "  服务器的id为：", i.uuid, "  服务器的cpu为：", str(i.cpu_sum)+"核", "  服务器的mem为："
                     , str(i.mem_sum)+"G", "  服务器已使用cpu为：" , str(i.cpu_used)+"核",  "  服务器已使用mem为：" , str(i.mem_used)+"G",
                  "  服务器的状态为：", i.status)
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()
        print("物理链路资源使用情况为：")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

        host_link_list = self.host_link_list
        for i in host_link_list:
            print("  物理链路的名字为：", i.name, "  物理链路的id为：", i.uuid, "  物理链路的端点为：", i.node1_name+"和"+i.node2_name,
                  "  物理链路的带宽总量为：", str(i.bandwidth_sum)+"Gbit/s", "  物理链路的带宽使用量为：", str(i.bandwidth_used)+"Gbit/s")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print()

if __name__ == "__main__":
    d = Datacenter()
    d.init_datacenter_network()
    # print(d.host_list)
    # print(d.host_link_list)
    # d.get_avail_host_list(11)
    # for i in d.get_sleep_host_list():
    #     print(i.name, i.uuid, i.cpu_sum, i.mem_sum, i.cpu_used, i.mem_used, i.status)

    # for i in d.host_link_list:
    #     print(i.name, i.uuid, i.node1_name, i.node2_name, i.bandwidth_sum, i.bandwidth_used)