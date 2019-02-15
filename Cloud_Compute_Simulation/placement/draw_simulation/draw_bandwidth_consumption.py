#coding=utf-8

import pylab as pl
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from placement.placement_VMSP import result_VMSP
from placement.placement_Random import result_Random
from placement.placement_BF import result_BF
from placement.placement_OS import result_Openstack
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
mpl.rcParams['font.sans-serif'] = ['SimHei']
xmajorLocator = MultipleLocator(4) #将y轴主刻度标签设置为4的倍数
ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度

def deal(lista):
    liatb = []
    for i in lista:
        liatb.append(i/2)
    return liatb

def draw_bandwidth_consumption():
    vm_number_list_VMSP = result_VMSP.get_vm_number_list()
    bandwidth_consumption_list_VMSP = [0, 50, 140, 190, 240, 350, 462, 552, 602, 652]

    vm_number_list_Random = result_Random.get_vm_number_list()
    bandwidth_consumption_list_Random = [0, 344, 644, 959, 1159, 1509, 1959, 2209, 2409, 2634]

    vm_number_list_BF = result_BF.get_vm_number_list()
    bandwidth_consumption_list_BF = [0, 100, 240, 340, 440, 600, 762, 902, 1002, 1102]

    vm_number_list_Openstack = result_Openstack.get_vm_number_list()
    bandwidth_consumption_list_Openstack = [0, 262, 462, 642, 742, 992, 1292, 1442, 1542, 1667]

    pl.plot(vm_number_list_VMSP, deal(bandwidth_consumption_list_VMSP), 'ob-', label=u'VMSP')
    pl.plot(vm_number_list_Random, deal(bandwidth_consumption_list_Random), '^g--', label=u'BA')
    pl.plot(vm_number_list_BF, deal(bandwidth_consumption_list_BF), 'sr-.', label=u'BF')
    pl.plot(vm_number_list_Openstack, deal(bandwidth_consumption_list_Openstack), 'vk:', label=u'OS')

    pl.xlabel(u"虚拟机的数量(个)")
    pl.ylabel(u"云数据中心的链路资源消耗(Mbit/s)")
    pl.title(u"不同算法下虚拟机的数量和云数据中心的链路资源消耗的关系")
    pl.legend()  # 让图例生效
    pl.show()

if (__name__=="__main__"):
    draw_bandwidth_consumption()