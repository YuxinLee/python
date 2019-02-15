# -*- coding: utf-8 -*-

import web
import json
import Engine
from setting import logger
import threading

urls=(
    '/request','CloudService'
)

class CloudService(object):

    def __algorithmDemo(self, servicename, cpu, memory, storage):
        '''
        输入参数
        :param servicename:     服务名字
        :param cpu:             CPU需求
        :param memory:          内存需求
        :param storage:         硬盘需求
        返回值
        :return:                映射结果
        '''
        '''
        分配算法
        '''
        num = int(memory) / 512
        ret = []
        for i in range(num):
            d = dict()
            d['instance_name'] = servicename + str(i)
            d['flavor'] = 'm1.tiny'
            d['image'] = 'cirros-0.3.3-x86_64'
            d['nic'] = '72c563de-d9ee-48f9-82bb-2ce1360c94a7'
            d['zone'] = 'zone_test1'
            if i % 2 == 0:
                d['node'] = 'compute1'
            else:
                d['node'] = 'compute2'
            ret.append(d)
        return ret


    def __RunWithAlgorithm(self, servicename, cpu, memory, storage, algorithm):
        '''
        if algorithm == "":
            r = self.__algorithm(servicename, cpu, memory, storage)
        elif algorithm == "":
            #
        else:
            #
        '''

        #现在没有算法，先用一个demo做示范
        r = self.__algorithmDemo(servicename, cpu, memory, storage)
        e = Engine.Engine()
        e.connectToController()
        for info in r:
            flavor = info['flavor']
            image = info['image']
            nic = info['nic']
            zone = info['zone']
            node = info['node']
            name = info['instance_name']
            ret = e.deployVMtoMachine(flavor_name=flavor, image_name=image,
                                nic_id=nic, zone_name=zone, machine_name=node, instanc_name=name)
        e.close()


    def __deleteVM(self, uuid):
        e = Engine.Engine()
        e.connectToController()
        e.deleteVM(uuid)
        e.close()

    def POST(self):
        i = web.input()
        r = json.loads(json.dumps(i))
        print r['serviceName'], r['memory'], r['cpu'], r['storage']
        serviceName = r['serviceName']
        memory = r['memory']
        cpu = r['cpu']
        storage = r['cpu']
        algorithm = r['algorithm']
        #self.__RunWithAlgorithm(servicename=serviceName, memory=memory,cpu=cpu, storage=storage, algorithm=algorithm)
        t = threading.Thread(target=CloudService.__RunWithAlgorithm, args=(self, serviceName, cpu, memory, storage, algorithm))
        t.start()
        return "running"



    def GET(self):
        r = web.input()
        r = json.loads(json.dumps(r))
        if r['operation'] == 'delete':
            if r['uuid'] != '':
                t = threading.Thread(target=CloudService.__deleteVM, args=(self, r['uuid']))
                t.start()
        return "deleting"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()