#coding=utf-8

class Vm:
    def __init__(self, vm_name, vm_cpu, vm_mem, vm_disk, vm_host = "default"):
        self.__vm_name = vm_name
        self.__vm_cpu = vm_cpu
        self.__vm_mem = vm_mem
        self.__vm_disk = vm_disk
        self.__vm_host = vm_host


    def get_vm_name(self):
        return self.__vm_name


    def get_vm_cpu(self):
        return self.__vm_cpu

    def get_vm_mem(self):
        return self.__vm_mem

    def get_vm_disk(self):
        return self.__vm_disk

    def get_vm_host(self):
        return self.__vm_host

    def set_vm_host(self,value):
        self.__vm_host = value


