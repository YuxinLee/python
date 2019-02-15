#coding=utf-8

#coding=utf-8

import pylab as pl
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
mpl.rcParams['font.sans-serif'] = ['SimHei']
ymajorLocator = MultipleLocator(2) #将y轴主刻度标签设置为4的倍数
ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度
xmajorLocator = MultipleLocator(4) #将y轴主刻度标签设置为4的倍数
ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度
from placement.placement_VMSP import result_VMSP
from placement.placement_Random import result_Random
from placement.placement_BF import result_BF
from placement.placement_OS import result_Openstack

def draw_active_host_num():
    # vm_number_list_VMSP = result_VMSP.get_vm_number_list()
    # active_host_num_list_VMSP = result_VMSP.get_active_host_num_list()
    #
    # vm_number_list_Random = result_Random.get_vm_number_list()
    # active_host_num_list_Random = result_Random.get_active_host_num_list()
    #
    # vm_number_list_BF = result_BF.get_vm_number_list()
    # active_host_num_list_BF = result_BF.get_active_host_num_list()
    #
    # vm_number_list_Openstack = result_Openstack.get_vm_number_list()
    # active_host_num_list_Openstack = result_Openstack.get_active_host_num_list()

    b = [1, 2, 4, 6, 7, 9, 9, 9, 9, 9]
    c = [1, 1, 2, 3, 3, 4, 4, 5, 6, 6]
    d = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7]
    vm_number_list_VMSP = [1,4,6,9,10,12,15,17,18,20]
    active_host_num_list_VMSP =[1, 1, 1, 2, 2, 3, 3, 3, 4, 4]

    vm_number_list_Random = [1,4,6,9,10,12,15,17,18,20]
    active_host_num_list_Random =[1, 2, 4, 6, 7, 9, 9, 9, 9, 9]

    vm_number_list_BF =[1,4,6,9,10,12,15,17,18,20]
    active_host_num_list_BF =[1, 1, 2, 3, 3, 4, 4, 5, 6, 6]

    vm_number_list_Openstack = [1,4,6,9,10,12,15,17,18,20]
    active_host_num_list_Openstack =[1, 2, 3, 4, 5, 5, 5, 6, 7, 7]


    pl.plot(vm_number_list_VMSP, active_host_num_list_VMSP, 'ob-', label=u'VMSP')
    pl.plot(vm_number_list_Random, active_host_num_list_Random, '^g--', label=u'BA')
    pl.plot(vm_number_list_BF, active_host_num_list_BF, 'sr-.', label=u'BF')
    pl.plot(vm_number_list_Openstack, active_host_num_list_Openstack, 'vk:', label=u'OS')
    pl.xlabel(u"虚拟机的数量(个)")
    pl.ylabel(u"云数据中心活跃服务器的数量(个)")
    pl.title(u"不同算法下虚拟机的数量和云数据中心活跃服务器的数量关系")
    pl.legend()  # 让图例生效
    pl.show()

if (__name__=="__main__"):
    draw_active_host_num()