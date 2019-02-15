#coding=utf-8

import pylab as pl
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
xmajorLocator = MultipleLocator(4) #将y轴主刻度标签设置为4的倍数
ax = subplot(111) #注意:一般都在ax中设置,不再plot中设置
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度
from placement.placement_VMSP import result_1_1
from placement.placement_VMSP import result_5_1
from placement.placement_VMSP import result_1_5

def deal(lista):
    value=0
    liatb = []
    for i in lista:
        liatb.append(i+value)
        value = value + 50
    return liatb

def draw_bandwidth_consumption():
    # vm_number_list_1_1 = result_1_1.get_vm_number_list()
    # bandwidth_consumption_list_1_1 = result_1_1.get_bandwidth_consumption_list()
    #
    # vm_number_list_5_1 = result_5_1.get_vm_number_list()
    # bandwidth_consumption_list_5_1 = result_5_1.get_bandwidth_consumption_list()
    #
    # vm_number_list_1_5 = result_1_5.get_vm_number_list()
    # bandwidth_consumption_list_1_5 = result_1_5.get_bandwidth_consumption_list()

    vm_number_list_1_1 = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    bandwidth_consumption_list_1_1 = [0.0, 16.0, 16.0, 96.0, 96.0, 275.0, 358.0, 358.0, 358.0, 519.0]

    vm_number_list_5_1 = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    bandwidth_consumption_list_5_1 = [0.0, 16.0, 36.0, 151.0, 151.0, 338.0, 394.0, 399.0, 399.0, 696.0]

    vm_number_list_1_5 = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    bandwidth_consumption_list_1_5 = [0.0, 16.0, 16.0, 16.0, 16.0, 179.0, 179.0, 179.0, 179.0, 290.0]

    pl.plot(vm_number_list_1_1, deal(bandwidth_consumption_list_1_1), 'ob-', label=u'VMSP_1_1')
    pl.plot(vm_number_list_5_1, deal(bandwidth_consumption_list_5_1), '^g--', label=u'VMSP_5_1')
    pl.plot(vm_number_list_1_5, deal(bandwidth_consumption_list_1_5), 'sr-.', label=u'VMSP_1_5')
    pl.xlabel(u"虚拟机的数量(个)")
    pl.ylabel(u"云数据中心的链路资源消耗(Mbit/s)")
    pl.title(u"不同权值下虚拟机的数量和云数据中心的链路资源消耗的关系")
    pl.legend()  # 让图例生效
    pl.show()




if (__name__=="__main__"):
    draw_bandwidth_consumption()