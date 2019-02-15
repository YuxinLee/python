#coding=utf-8

import pylab as pl
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from placement.placement_VMSP import result_VMSP
from placement.placement_Random import result_Random
from placement.placement_BF import result_BF
from placement.placement_OS import result_Openstack
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
# mpl.rcParams['font.sans-serif'] = ['SimHei']
xmajorLocator = MultipleLocator(4) #将y轴主刻度标签设置为4的倍数
ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度

def deal(lista):
    value=0
    liatb = []
    for i in lista:
        liatb.append(i+value)
        value = value + 100
    return liatb

def draw_power_consumption():
    # vm_number_list_VMSP = result_VMSP.get_vm_number_list()
    # power_consumption_list_VMSP = result_VMSP.get_power_consumption_list()
    #
    # vm_number_list_Random = result_Random.get_vm_number_list()
    # power_consumption_list_Random = result_Random.get_power_consumption_list()
    #
    # vm_number_list_BF = result_BF.get_vm_number_list()
    # power_consumption_list_BF = result_BF.get_power_consumption_list()
    #
    # vm_number_list_Openstack = result_Openstack.get_vm_number_list()
    # power_consumption_list_Openstack = result_Openstack.get_power_consumption_list()
    vm_number_list_VMSP = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    active_host_num_list_VMSP = [400, 400, 400, 800, 800, 1200, 1200, 1200, 1600, 1600]

    vm_number_list_Random = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    active_host_num_list_Random = [400, 800, 1600, 2400, 2800, 3600, 3600, 3600, 3600, 3600]

    vm_number_list_BF = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    active_host_num_list_BF = [400, 400, 800, 1200, 1200, 1600, 1600, 2000, 2400, 2400]

    vm_number_list_Openstack = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    active_host_num_list_Openstack = [400, 800, 1200, 1600, 2000, 2000, 2000, 2400, 2800, 2800]

    pl.plot(vm_number_list_VMSP, deal(active_host_num_list_VMSP) , 'ob-', label=u'VMSP')
    pl.plot(vm_number_list_Random, deal(active_host_num_list_Random), '^g--', label=u'BA')
    pl.plot(vm_number_list_BF, deal(active_host_num_list_BF), 'sr-.', label=u'BF')
    pl.plot(vm_number_list_Openstack, deal(active_host_num_list_Openstack), 'vk:', label=u'OS')

    pl.xlabel(u"虚拟机的数量(个)")
    pl.ylabel(u"云数据中心的功耗(w)")
    pl.title(u"不同算法下虚拟机的数量和云数据中心功耗的关系")
    pl.legend()  # 让图例生效
    pl.show()

if (__name__=="__main__"):
    draw_power_consumption()