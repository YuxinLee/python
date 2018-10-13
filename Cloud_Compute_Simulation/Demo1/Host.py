#coding=utf-8

class Host:
    def __init__(self, host_name, cpu_sum, mem_sum, cpu_used, mem_used, status="sleep"):

        self.__host_name = host_name
        self.__cpu_sum = cpu_sum
        self.__mem_sum = mem_sum
        self.__cpu_used = cpu_used
        self.__mem_used = mem_used
        self.__status = status

    def get_host_name(self):
        return self.__host_name

    def get_host_cpu_sum(self):
        return self.__cpu_sum

    def get_host_mem_sum(self):
        return self.__mem_sum

    def get_host_status(self):
        return self.__status

    def get_host_mem_used(self):
        return self.__mem_used

    def set_host_mem_used(self, value):
        self.__mem_used = value

    def set_host_cpu_used(self, value):
        self.__cpu_used = value

    def get_host_cpu_used(self):
        return self.__cpu_used

    def set_host_status(self, value):
        self.__status = value