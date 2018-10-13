#coding=utf-8



def get_host_energy_consumption(host):
    if(host.get_host_status() == "sleep"):
        return 0.0
    if(host.get_host_status() == "alive"):
        host_cpu_used = host.get_host_cpu_used()
        host_mem_used = host.get_host_mem_used()
        host_cpu_sum = host.get_host_cpu_sum()
        host_mem_sum = host.get_host_mem_sum()

        host_full_energy_consumption = 500.0
        host_cpu_full_energy_consumption = host_full_energy_consumption * 0.8
        host_mem_full_energy_consumption = host_full_energy_consumption * 0.2

        #服务器空闲时能源消耗为20%
        host_idle_energy_consumption = 500.0 * 0.2
        host_cpu_idle_energy_consumption = host_idle_energy_consumption * 0.8
        host_mem_idle_energy_consumption = host_idle_energy_consumption * 0.2

        host_cpu_actual_energy_consumption = (host_cpu_full_energy_consumption-host_cpu_idle_energy_consumption) * \
                                             (1.0 * host_cpu_used / host_cpu_sum) + host_cpu_idle_energy_consumption

        host_mem_actual_energy_consumption = (host_mem_full_energy_consumption - host_mem_idle_energy_consumption) * \
                                             (1.0 * host_mem_used / host_mem_sum) + host_mem_idle_energy_consumption

        host_actual_energy_consumption = host_cpu_actual_energy_consumption + host_mem_actual_energy_consumption
        return host_actual_energy_consumption

def get_datacenter_energy_consumption(host_list):
    total_energy_consumption = 0.0
    host_number = len(host_list)
    for i in range(host_number):
        total_energy_consumption = total_energy_consumption + get_host_energy_consumption(host_list[i])

    return total_energy_consumption
