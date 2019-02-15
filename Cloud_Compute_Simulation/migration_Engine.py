#coding=utf-8

import paramiko

def migration_vm(vm_name, host_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect("192.168.1.10", 22, 'root', 'cloud')
    login_cmd = ". admin-openrc"
    migration_vm_cmd = "nova live-migration " + vm_name + " " + host_name
    # print(migration_vm_cmd)
    ssh.exec_command(login_cmd + "&&" + migration_vm_cmd)
    # migration_vm("vm7", "compute2")






