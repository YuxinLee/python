# -*- coding: utf-8 -*-
import requests
import paramiko
import MySQLdb
import time
from setting import logger

logincmd = 'source admin-openrc.sh'
novaflavor = 'nova flavor-list'
novaimage = 'nova image-list'
novanic = 'neutron net-list'
result = 'nova list'
novasecgroup = 'nova secgroup-list'
novaboot = 'nova boot --flavor m1.tiny --image cirros-0.3.3-x86_64 --nic net-id=6aace909-40d4-42d7-9d04-5172c9b05e64' \
           ' --security-group default ' '--availability-zone zone_test1:compute1 ' \
           'demoName2'


class Engine(object):
    def __init__(self):
        self.host = '192.168.1.20'
        self.port = 22
        self.username = 'xin'
        self.passwd = '0421'
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def close(self):
        self.ssh.close()

    def __buildDeployCmd(self, nodename):
        pass

    def connectToController(self):
        try:
            self.ssh.connect(self.host, self.port, self.username, self.passwd)
        except Exception:
            pass

    '''
    +--------------------------------------+------------------------------------------------------------+
    
    | Property                             | Value                                                      |
    
    +--------------------------------------+------------------------------------------------------------+
    
    | OS-DCF:diskConfig                    | MANUAL                                                     |
    
    | OS-EXT-AZ:availability_zone          | nova                                                       |
    
    | OS-EXT-SRV-ATTR:host                 | -                                                          |
    
    | OS-EXT-SRV-ATTR:hypervisor_hostname  | -                                                          |
    
    | OS-EXT-SRV-ATTR:instance_name        | instance-00000045                                          |
    
    | OS-EXT-STS:power_state               | 0                                                          |
    
    | OS-EXT-STS:task_state                | scheduling                                                 |
    
    | OS-EXT-STS:vm_state                  | building                                                   |
    
    | OS-SRV-USG:launched_at               | -                                                          |
    
    | OS-SRV-USG:terminated_at             | -                                                          |
    
    | accessIPv4                           |                                                            |
    
    | accessIPv6                           |                                                            |
    
    | adminPass                            | Mu6eVnTuT497                                               |
    
    | config_drive                         |                                                            |
    
    | created                              | 2017-12-23T14:32:17Z                                       |
    
    | flavor                               | m1.tiny (1)                                                |
    
    | hostId                               |                                                            |
    
    | id                                   | 0e3cde5a-bceb-425e-b50d-a935953db490                       |
    
    | image                                | cirros-0.3.3-x86_64 (56401d6b-8c54-43c5-a708-51ef5353c789) |
    
    | key_name                             | -                                                          |
    
    | metadata                             | {}                                                         |
    
    | name                                 | demoName2                                                  |
    
    | os-extended-volumes:volumes_attached | []                                                         |
    
    | progress                             | 0                                                          |
    
    | security_groups                      | default                                                    |
    
    | status                               | BUILD                                                      |
    
    | tenant_id                            | 5fe9d3cba0b2493da411f55812bae095                           |
    
    | updated                              | 2017-12-23T14:32:17Z                                       |
    
    | user_id                              | 3ff50ed46bf34d9dbb113de8ca579b33                           |
    
    +--------------------------------------+------------------------------------------------------------+
    
    # [u'+--------------------------------------+------------------------------------------------------------+\n']
    # [u'', u' Property                             ', u' Value                                                      ', u'\n']
    # [u'+--------------------------------------+------------------------------------------------------------+\n']
    # [u'', u' OS-DCF:diskConfig                    ', u' MANUAL                                                     ', u'\n']
    # [u'', u' OS-EXT-AZ:availability_zone          ', u' nova                                                       ', u'\n']
    # [u'', u' OS-EXT-SRV-ATTR:host                 ', u' -                                                          ', u'\n']
    # [u'', u' OS-EXT-SRV-ATTR:hypervisor_hostname  ', u' -                                                          ', u'\n']
    # [u'', u' OS-EXT-SRV-ATTR:instance_name        ', u' instance-00000046                                          ', u'\n']
    # [u'', u' OS-EXT-STS:power_state               ', u' 0                                                          ', u'\n']
    # [u'', u' OS-EXT-STS:task_state                ', u' scheduling                                                 ', u'\n']
    # [u'', u' OS-EXT-STS:vm_state                  ', u' building                                                   ', u'\n']
    # [u'', u' OS-SRV-USG:launched_at               ', u' -                                                          ', u'\n']
    # [u'', u' OS-SRV-USG:terminated_at             ', u' -                                                          ', u'\n']
    # [u'', u' accessIPv4                           ', u'                                                            ', u'\n']
    # [u'', u' accessIPv6                           ', u'                                                            ', u'\n']
    # [u'', u' adminPass                            ', u' aob35dEmeGQu                                               ', u'\n']
    # [u'', u' config_drive                         ', u'                                                            ', u'\n']
    # [u'', u' created                              ', u' 2017-12-23T14:35:16Z                                       ', u'\n']
    # [u'', u' flavor                               ', u' m1.tiny (1)                                                ', u'\n']
    # [u'', u' hostId                               ', u'                                                            ', u'\n']
    # [u'', u' id                                   ', u' a7b05806-e279-4501-bdaa-24d7d54c8b49                       ', u'\n']
    # [u'', u' image                                ', u' cirros-0.3.3-x86_64 (56401d6b-8c54-43c5-a708-51ef5353c789) ', u'\n']
    # [u'', u' key_name                             ', u' -                                                          ', u'\n']
    # [u'', u' metadata                             ', u' {}                                                         ', u'\n']
    # [u'', u' name                                 ', u' demoName2                                                  ', u'\n']
    # [u'', u' os-extended-volumes:volumes_attached ', u' []                                                         ', u'\n']
    # [u'', u' progress                             ', u' 0                                                          ', u'\n']
    # [u'', u' security_groups                      ', u' default                                                    ', u'\n']
    # [u'', u' status                               ', u' BUILD                                                      ', u'\n']
    # [u'', u' tenant_id                            ', u' 5fe9d3cba0b2493da411f55812bae095                           ', u'\n']
    # [u'', u' updated                              ', u' 2017-12-23T14:35:16Z                                       ', u'\n']
    # [u'', u' user_id                              ', u' 3ff50ed46bf34d9dbb113de8ca579b33                           ', u'\n']
    # [u'+--------------------------------------+------------------------------------------------------------+\n']
    
    '''
    '''
    暂不解析结果，直接从数据库中读取
    '''
    def deployVM(self):
        _, stdout, stderr = self.ssh.exec_command(logincmd + '&&' + novaboot)
        if stderr.readlines() == []:
            for str in stdout.readlines():
                #print str
                strList = str.split('|')
                print '#' , strList
            return True
        else:
            for str in stderr.readlines():
                print str
            return False

    'nova boot --flavor m1.tiny --image cirros-0.3.3-x86_64 --nic net-id=6aace909-40d4-42d7-9d04-5172c9b05e64' \
    ' --security-group default ' '--availability-zone zone_test1:compute1 ' \
    'demoName2'
    def deployVMtoMachine(self, flavor_name, image_name, nic_id, zone_name, machine_name, instanc_name):
        __novaboot = 'nova boot --flavor %s --image %s --nic net-id=%s ' \
                     '--security-group default --availability-zone %s:%s %s'%\
                     (flavor_name, image_name, nic_id, zone_name, machine_name, instanc_name)
        cmd = logincmd + '&&' + __novaboot
        print cmd
        _, stdout, stderr = self.ssh.exec_command(logincmd + ' && ' + __novaboot)
        stderrArr = stderr.readlines()
        if stderrArr == []:
            for str in stdout.readlines():
                logger.info(str)
            return True
        else:
            for str in stderrArr:
                logger.error(str)
            return False

    def deleteVM(self, uuid):
        __deletecmd = '%s && nova delete %s'%(logincmd, uuid)
        _, stdout, stderr = self.ssh.exec_command(__deletecmd)
        if stderr.readlines() == []:
            for str in stdout.readlines():
                print str
        else:
            for str in stderr.readlines():
                print str
