#coding=utf-8

def get_active_host_number(host_list):
    active_host_number = 0
    for i in host_list:
        if(i.status == "active"):
            active_host_number = active_host_number + 1
    return active_host_number