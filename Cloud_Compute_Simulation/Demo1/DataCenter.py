#coding=utf-8

#网络拓扑中包括的节点为6个交换机和8个服务器
#3个交换机分别为 核心交换机s1 ， 核心交换机s2， 接入交换机s3，接入交换机s4，接入交换机s5，接入交换机s6
#5个服务器：compute1，compute2，compute3，compute4，compute5，compute6，compute7，compute8
"""
网络拓扑图为：
                            核心交换机s1                           100000                              核心交换机s2

                        10000                        10000                                        10000                    10000

                    接入交换机s3             接入交换机s4                                 接入交换机s5             接入交换机s6

            1000            1000            1000            1000                        1000            1000            1000           1000

        compute1        compute2    |   compute3        compute4                    compute5        compute6    |   compute7        compute8
"""

import networkx as nx
from Demo1 import Host
import matplotlib.pyplot as plt

g = nx.Graph()
g.clear()
g.graph["name"] = "工业云数据中心网络拓扑"

host_list = []      #服务器列表

def init_datacenter():

    # 定义服务器
    compute1 = Host.Host("compute1", 64, 128, 0, 0)
    compute2 = Host.Host("compute2", 64, 128, 0, 0)
    compute3 = Host.Host("compute3", 64, 128, 0, 0)
    compute4 = Host.Host("compute4", 64, 128, 0, 0)
    compute5 = Host.Host("compute5", 64, 128, 0, 0)
    compute6 = Host.Host("compute6", 64, 128, 0, 0)
    compute7 = Host.Host("compute7", 64, 128, 0, 0)
    compute8 = Host.Host("compute8", 64, 128, 0, 0)

    # 创建服务器列表
    host_list.append(compute1)
    host_list.append(compute2)
    host_list.append(compute3)
    host_list.append(compute4)
    host_list.append(compute5)
    host_list.append(compute6)
    host_list.append(compute7)
    host_list.append(compute8)

    # 添加节点
    g.add_node("核心交换机s1")
    g.add_node("核心交换机s2")
    g.add_node("接入交换机s3")
    g.add_node("接入交换机s4")
    g.add_node("接入交换机s5")
    g.add_node("接入交换机s6")
    g.add_node("compute1")
    g.add_node("compute2")
    g.add_node("compute3")
    g.add_node("compute4")
    g.add_node("compute5")
    g.add_node("compute6")
    g.add_node("compute7")
    g.add_node("compute8")

    # 添加边
    g.add_edge("核心交换机s1", "核心交换机s2", bandwidth=100000)
    # print(g["核心交换机s1"]["核心交换机s2"]["bandwidth"])

    g.add_edge("核心交换机s1", "接入交换机s3", bandwidth=10000)
    g.add_edge("核心交换机s1", "接入交换机s4", bandwidth=10000)

    g.add_edge("核心交换机s2", "接入交换机s5", bandwidth=10000)
    g.add_edge("核心交换机s2", "接入交换机s6", bandwidth=10000)

    g.add_edge("接入交换机s3", "compute1", bandwidth=1000)
    g.add_edge("接入交换机s3", "compute2", bandwidth=1000)

    g.add_edge("接入交换机s4", "compute3", bandwidth=1000)
    g.add_edge("接入交换机s4", "compute4", bandwidth=1000)

    g.add_edge("接入交换机s5", "compute5", bandwidth=1000)
    g.add_edge("接入交换机s5", "compute6", bandwidth=1000)

    g.add_edge("接入交换机s6", "compute7", bandwidth=1000)
    g.add_edge("接入交换机s6", "compute8", bandwidth=1000)

    #print (list(nx.all_simple_paths(g,"compute1","compute1"))==[])
    # g["compute1"]["接入交换机s3"]["bandwidth"] = g["compute1"]["接入交换机s3"]["bandwidth"] - 100
    # print(g["compute1"]["接入交换机s3"]["bandwidth"])

    # for i in nx.all_simple_paths(g,"compute1","compute8"):
    #     print(i)



    # nx.draw(g)
    # plt.show()

def get_host_list():
    return host_list

def get_alive_host_list():
    alive_host_list = []
    for i in host_list:
        if (i.get_host_status() == "alive"):
            alive_host_list.append(i)
    return alive_host_list

def get_sleep_host_list():
    sleep_host_list = []
    for i in host_list:
        if(i.get_host_status() == "sleep"):
            sleep_host_list.append(i)
    return sleep_host_list

def get_network_graph():
    return g

# init_datacenter()
# print(get_host_list())
# print(get_sleep_host_list())







