#coding=utf-8

from Demo1 import DataCenter

#DataCenter.init_datacenter()
host_list = DataCenter.get_host_list()

def show_all_host_info(host_list):
    for i in range(len(host_list)):
        print("主机名："+str(host_list[i].get_host_name())+"      "+"总cpu为："+str(host_list[i].get_host_cpu_sum())+"      "+"总mem为："+str(host_list[i].get_host_mem_sum())
              +"      "+"已使用cpu："+str(host_list[i].get_host_cpu_used())+"      "+"已使用mem："+str(host_list[i].get_host_mem_used())+"       "+"主机状态为："+str(host_list[i].get_host_status()))


if __name__ == "__main__":
    show_all_host_info(host_list)

