#coding=utf-8

#coding=utf-8

import pylab as pl
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
mpl.rcParams['font.sans-serif'] = ['SimHei']
ymajorLocator = MultipleLocator(3) #将y轴主刻度标签设置为4的倍数
ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度
from migration.migration_VMDM import result_VMDM
from migration.migration_ST import result_ST
from migration.migration_DT import result_DT


def draw_active_host_num():
    timestamps_list_VMDM = result_VMDM.get_timestamps_list()
    active_host_num_list_VMDM = result_VMDM.get_active_host_num_list()

    timestamps_list_ST = result_ST.get_timestamps_list()
    active_host_num_list_ST = result_ST.get_active_host_num_list()

    timestamps_list_DT = result_DT.get_timestamps_list()
    active_host_num_list_DT = result_DT.get_active_host_num_list()

    # vm_number_list_Random = result_Random.get_vm_number_list()
    # active_host_num_list_Random = result_Random.get_active_host_num_list()
    #
    # vm_number_list_Balance = result_Balance.get_vm_number_list()
    # active_host_num_list_Balance = result_Balance.get_active_host_num_list()
    #
    # vm_number_list_Openstack = result_Openstack.get_vm_number_list()
    # active_host_num_list_Openstack = result_Openstack.get_active_host_num_list()

    pl.plot(timestamps_list_VMDM, active_host_num_list_VMDM, 'ob-', label=u'VMDM')
    pl.plot(timestamps_list_ST, active_host_num_list_ST, '^g--', label=u'ST')
    pl.plot(timestamps_list_DT, active_host_num_list_DT, 'sr-.', label=u'DT')
    # pl.plot(vm_number_list_Openstack, active_host_num_list_Openstack, 'vk:', label=u'OpenStack')
    pl.xlabel(u"时间(时)")
    pl.ylabel(u"云数据中心活跃服务器的数量(个)")
    pl.title(u"不同算法下云数据中心运行的时间和活跃服务器的数量关系")
    pl.legend()  # 让图例生效
    pl.show()

if (__name__=="__main__"):
    draw_active_host_num()