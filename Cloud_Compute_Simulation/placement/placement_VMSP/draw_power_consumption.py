#coding=utf-8

import pylab as pl
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from placement.placement_VMSP import result_1_1
from placement.placement_VMSP import result_5_1
from placement.placement_VMSP import result_1_5
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
    # vm_number_list_1_1 = result_1_1.get_vm_number_list()
    # power_consumption_list_1_1 = result_1_1.get_power_consumption_list()
    #
    # vm_number_list_5_1 = result_5_1.get_vm_number_list()
    # power_consumption_list_5_1 = result_5_1.get_power_consumption_list()
    #
    # vm_number_list_1_5 = result_1_5.get_vm_number_list()
    # power_consumption_list_1_5 = result_1_5.get_power_consumption_list()
    vm_number_list_1_1 = [1,4,6,9,10,12,15,17,18,20]
    power_consumption_list_1_1 = [106.25, 450.0, 606.25, 643.75, 693.75, 1318.75, 1368.75, 1381.25, 1568.75, 1612.5]


    vm_number_list_5_1 = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    power_consumption_list_5_1 = [106.25, 450.0, 506.25, 543.75, 593.75, 1118.75, 1168.75, 1181.25, 1268.75, 1312.5]

    vm_number_list_1_5 = [1, 4, 6, 9, 10, 12, 15, 17, 18, 20]
    power_consumption_list_1_5 = [106.25, 450.0, 606.25, 643.75, 793.75, 1418.75, 1468.75, 1481.25, 1668.75, 1712.5]


    pl.plot(vm_number_list_1_1, deal(power_consumption_list_1_1), 'ob-', label=u'VMSP_1_1')
    pl.plot(vm_number_list_5_1, deal(power_consumption_list_5_1), '^g--', label=u'VMSP_5_1')
    pl.plot(vm_number_list_1_5, deal(power_consumption_list_1_5), 'sr-.', label=u'VMSP_1_5')
    pl.xlabel(u"虚拟机的数量(个)")
    pl.ylabel(u"云数据中心的功耗(w)")
    pl.title(u"不同权值下虚拟机的数量和云数据中心功耗的关系")
    pl.legend()  # 让图例生效
    pl.show()




if (__name__=="__main__"):
    draw_power_consumption()