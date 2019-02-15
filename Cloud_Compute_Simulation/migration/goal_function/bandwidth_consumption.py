#coding=utf-8

import networkx as nx

def get_datacenter_bandwidth_consumption(g, host_link_list):
    total_bandwidth_consumption = 0
    for i in host_link_list:
        node1_name = i.node1_name
        node2_name = i.node2_name
        bandwidth_used = i.bandwidth_used
        node_link_list = list(nx.all_simple_paths(g, node1_name, node2_name))
        if (node_link_list == []):
            continue
        total_bandwidth_consumption = total_bandwidth_consumption + (len(node_link_list[0]) - 1) * bandwidth_used
    return total_bandwidth_consumption