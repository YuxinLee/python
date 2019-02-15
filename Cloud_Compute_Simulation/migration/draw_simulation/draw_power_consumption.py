#coding=utf-8

import pylab as pl
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from migration.migration_VMDM import result_VMDM
from migration.migration_ST import result_ST
from migration.migration_DT import result_DT

def draw_power_consumption():
    timestamps_list_VMDM = result_VMDM.get_timestamps_list()
    power_consumption_list_VMDM = result_VMDM.get_power_consumption_list()

    timestamps_list_ST = result_ST.get_timestamps_list()
    power_consumption_list_ST = result_ST.get_power_consumption_list()

    timestamps_list_DT = result_DT.get_timestamps_list()
    power_consumption_list_DT = result_DT.get_power_consumption_list()


    # vm_number_list_VMSP = result_VMSP.get_vm_number_list()
    # power_consumption_list_VMSP = result_VMSP.get_power_consumption_list()
    #
    # vm_number_list_Random = result_Random.get_vm_number_list()
    # power_consumption_list_Random = result_Random.get_power_consumption_list()
    #
    # vm_number_list_Balance = result_Balance.get_vm_number_list()
    # power_consumption_list_Balance = result_Balance.get_power_consumption_list()
    #
    # vm_number_list_Openstack = result_Openstack.get_vm_number_list()
    # power_consumption_list_Openstack = result_Openstack.get_power_consumption_list()

    pl.plot(timestamps_list_VMDM, power_consumption_list_VMDM, 'ob-', label=u'VMDM')
    pl.plot(timestamps_list_ST, power_consumption_list_ST, '^g--', label=u'ST')
    pl.plot(timestamps_list_DT, power_consumption_list_DT, 'sr-.', label=u'DT')
    # pl.plot(vm_number_list_Openstack, power_consumption_list_Openstack, 'vk:', label=u'OpenStack')

    pl.xlabel(u"时间(时)")
    pl.ylabel(u"云数据中心的功耗(w)")
    pl.title(u"不同算法下云数据中心运行的时间和功耗的关系")
    pl.legend()  # 让图例生效
    pl.show()

if (__name__=="__main__"):
    draw_power_consumption()