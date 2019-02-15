#coding=utf-8

import random

def placement_Random(host_list, vm):
    avail_host_list = []
    for i in host_list:
        host_cpu_used = i.cpu_used
        host_cpu_sum = i.cpu_sum
        host_mem_used = i.mem_used
        host_mem_sum = i.mem_sum
        if (((vm.cpu + host_cpu_used) * 1.0 / host_cpu_sum <= 0.6) and (
                (vm.mem + host_mem_used) * 1.0 / host_mem_sum <= 0.6)):
            avail_host_list.append(i)
    host = random.sample(avail_host_list, 1)[0]
    host.status = "active"
    host_cpu_used = host.cpu_used
    host_mem_used = host.mem_used
    host.cpu_used = host_cpu_used + vm.cpu
    host.mem_used = host_mem_used + vm.mem
    vm.hostname = host.name
    print("虚拟机", vm.name, "放置在服务器", vm.hostname, "中")







