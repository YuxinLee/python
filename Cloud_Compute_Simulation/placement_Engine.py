#coding=utf-8

import requests
import json
import uuid

OS_AUTH_URL = "http://192.168.1.10"
body = '''
{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "id": "7984a9af21434a0494cb755dc93ce41a",
                    "password": "cloud"
                }
            }
        },
        "scope": {
            "project": {
                "domain": {
                    "id": "default"
                },
                "name": "admin"
            }
        }
    }
}
'''
# http://192.168.1.10:35357/v3/auth/tokens
headers = {}
headers['Content-Type'] = 'application/json'
headers['Accept'] = '*/*'

"""
获取token
"""
def get_token():
    get_token_url = OS_AUTH_URL + ':35357/v3/auth/tokens'
    # result=requests.post(get_token_url,headers=headers,data=json.dumps(body)).headers['X-Subject-Token']
    result = requests.post(get_token_url, headers=headers, data=body).headers['X-Subject-Token']
    return result
# print(get_token())

"""
获取用户信息
"""
def get_user_info():
    user_list_url = OS_AUTH_URL + ':35357/v3/users'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(user_list_url, headers=headers).json()
    return (result)
# print(type(user_list()))
# print user_list()['users'][1]['links']

"""
获取image信息
"""
def get_images_info():
    images_list_url = OS_AUTH_URL + ':9292/v2/images'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(images_list_url, headers=headers).json()
    return result
# print(type(get_images_info()))

"""
获取image名字列表
"""
def get_images_name_list():
    images_name_list = []
    length = len(get_images_info()['images'])
    for i in range(length):
        images_name_list.append(get_images_info()['images'][i]['name'])
    return images_name_list
# print(get_images_name_list())

"""
获取server信息
"""
def get_servers_info():
    computes_list_url = OS_AUTH_URL + ':8774/v2.1/servers'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(computes_list_url, headers=headers).json()
    return (result)
# print(type(get_servers_info()))

"""
获取server信息
"""
def get_servers_detail_info():
    computes_list_url = OS_AUTH_URL + ':8774/v2.1/servers/detail'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(computes_list_url, headers=headers).json()
    return result
# print(get_servers_detail_info())

"""
获取server的名字列表
"""
def get_servers_name_list():
    servers_name_list = []
    length = len(get_servers_info()['servers'])
    for i in range(length):
        servers_name_list.append(get_servers_info()['servers'][i]['name'])
    return servers_name_list
# print(get_servers_name_list())

"""
获取flavor信息
"""
def get_flavors_info():
    flavors_list_url = OS_AUTH_URL + ':8774/v2.1/flavors'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(flavors_list_url, headers=headers).json()
    return result
# print(get_flavors_info())

"""
获取flavor名字列表
"""
def get_flavors_name_list():
    flavors_name_list = []
    length = len(get_flavors_info()['flavors'])
    for i in range(length):
        flavors_name_list.append(get_flavors_info()['flavors'][i]['name'])
    return flavors_name_list
# print(get_flavors_name_list())

"""
获取flavor名字列表
"""
def get_flavors_id_list():
    flavors_name_list = []
    length = len(get_flavors_info()['flavors'])
    for i in range(length):
        flavors_name_list.append(get_flavors_info()['flavors'][i]['id'])
    return flavors_name_list
# print(get_flavors_id_list())

"""
获取security_groups信息
"""
def get_security_groups_info():
    security_group_list_url = OS_AUTH_URL + ':8774/v2.1/os-security-groups'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(security_group_list_url, headers=headers).json()
    return result
# print(get_security_groups_info())

"""
获取security_groups名字列表
"""
def get_security_groups_name_list():
    security_groups_name_list = []
    length = len(get_security_groups_info()['security_groups'])
    for i in range(length):
        security_groups_name_list.append(get_security_groups_info()['security_groups'][i]['name'])
    return security_groups_name_list
# print(get_security_groups_name_list())

"""
获取network信息
"""
def get_networks_info():
    network_list_url = OS_AUTH_URL + ':9696/v2.0/networks'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(network_list_url, headers=headers).json()
    return result
# print(get_networks_info())

"""
获取network名字列表
"""
def get_networks_name_list():
    networks_name_list = []
    length = len(get_networks_info()['networks'])
    for i in range(length):
        networks_name_list.append(get_networks_info()['networks'][i]['name'])
    return networks_name_list
# print(get_networks_name_list())

"""
获取network的id列表
"""
def get_networks_id_list():
    networks_id_list = []
    length = len(get_networks_info()['networks'])
    for i in range(length):
        networks_id_list.append(get_networks_info()['networks'][i]['id'])
    return networks_id_list
# print(get_networks_id_list())

"""
获取subnet的信息
"""
def get_subnets_info():
    subnet_list_url = OS_AUTH_URL + ':9696/v2.0/subnets'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(subnet_list_url, headers=headers).json()
    return (result)
# print(get_subnets_info())

"""
获取subnet的名字列表
"""
def get_subnets_name_list():
    subnets_name_list = []
    length = len(get_subnets_info()['subnets'])
    for i in range(length):
        subnets_name_list.append(get_subnets_info()['subnets'][i]['name'])
    return subnets_name_list
# print(get_subnets_name_list())

"""
获取subnet的id列表
"""
def get_subnets_id_list():
    subnets_id_list = []
    length = len(get_subnets_info()['subnets'])
    for i in range(length):
        subnets_id_list.append(get_subnets_info()['subnets'][i]['id'])
    return subnets_id_list
# print(get_subnets_id_list())

"""
创建vm
"""
def create_vm():
    headers['X-Auth-Token'] = get_token()
    create_vm_url = OS_AUTH_URL + ':8774/v2.1/servers'
    create_vm_body = '''
    {
    "server": {
        "name": "test-007",
        "imageRef": "c29e761a-4ffb-4541-af44-0663bf130e5a",
        "flavorRef": "0",
        "networks" : [{
            "uuid" : "16f239d4-9999-438b-aabd-c3d31d08355a"

        }]
    }
}
    '''
    result = requests.post(create_vm_url, headers=headers, data=create_vm_body)
    # print (result.json())

def placement(vm_name, vm_cpu, vm_mem, vm_disk):
    flavor_id = get_flavorid(vm_cpu, vm_mem, vm_disk)
    if (flavor_id == None):
        print("SORRY，没有匹配的配置信息！！！")
        return
    create_vm(vm_name, flavor_id)

def create_vm(name, flavor_id):
    headers['X-Auth-Token'] = get_token()
    create_vm_url = OS_AUTH_URL + ':8774/v2.1/servers'
    create_vm_body = '''
    {
    "server": {
        "name": "%s",
        "imageRef": "7371d426-c03a-468b-94b8-b4462971c1f6",
        "flavorRef": "%s",
        "networks" : [{
            "uuid" : "aadad66a-338b-420a-93b6-7575cbd791f0"

        }]
    }
}
    ''' %(name, flavor_id)
    result = requests.post(create_vm_url, headers=headers, data=create_vm_body)
    # print (result.json())
# create_vm("vm1", "6614f4fa-f6f6-11e8-8398-1c1b0d5b7153")

"""
获取所有的版本
"""
def get_all_versons():
    flavors_list_url = OS_AUTH_URL + ':8774/'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(flavors_list_url, headers=headers).json()
    return result
# print(get_all_versons())

"""
    {
        "flavor": {
            "name": "test_flavor",
            "ram": 1024,
            "vcpus": 2,
            "disk": 10,
            "id": "10",
            "rxtx_factor": 2.0
        }
    }
    """

def service():
    while (True):
        string = input("请用户输入申请实例的数量：(1-1000)")
        if (not string.isdigit()):
            print("您输入有误！请重新输入！")
            continue
        number = int(string)
        if (number < 1):
            print("您输入有误！请重新输入！")
            continue
        elif (number == 1):
            print("请输入您的配置需求：实例名称，CPU资源，内存资源，磁盘空间")
            vm_name = input("实例名称：")
            vm_cpu = int(input("CPU资源(单位：核数)："))
            vm_mem = int(input("内存资源(单位：MB)："))
            vm_disk = int(input("磁盘空间(单位：GB)："))
            placement(vm_name, vm_cpu, vm_mem, vm_disk)
        else:
            vm_list = []
            for i in range(number):
                print("请输入您的第" + str(i + 1) + "个实例的配置需求：实例名称, CPU资源, 内存资源, 磁盘空间")
                vm_name = input("实例名称：")
                vm_cpu = int(input("CPU资源(单位：核数)："))
                vm_mem = int(input("内存资源(单位：MB)："))
                vm_disk = int(input("磁盘空间(单位：GB)："))
            vm_number = len(vm_list)
            for i in range(0, vm_number - 1, 1):
                for j in range(i + 1, vm_number, 1):
                    bandwidth = int(
                        input(("请输入") + vm_list[i].vm_name + "实例与" + vm_list[
                            j].vm_name + "实例的带宽需求："))

"""
创建flavors
"""
def create_flavors(name, ram, vcpus, disk, id):
    headers['X-Auth-Token'] = get_token()
    create_flavors_url = OS_AUTH_URL + ':8774/v2/flavors'
    create_flavors_body = """
    {
        "flavor": {
            "name": "%s",
            "ram": %d,
            "vcpus": %d,
            "disk": %d,
            "id": "%s",
            "rxtx_factor": 2.0
        }
    }
    """ %(name, ram, vcpus, disk, id)
    # print(create_flavors_body)
    result = requests.post(create_flavors_url, headers=headers, data=create_flavors_body)
    # print(result.json())
# create_flavors("m1.xlarge", 16384, 8, 160, str(uuid.uuid1()))

"""
删除flavor
"""
def delete_flavor(flavor_id):
    url = OS_AUTH_URL + ':8774/v2.1/flavors/%s' %flavor_id
    headers['X-Auth-Token'] = get_token()
    result = requests.delete(url, headers=headers)
    return result

def get_flavors_detail():
    flavors_list_url = OS_AUTH_URL + ':8774/v2.1/flavors/detail'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(flavors_list_url, headers=headers).json()
    return result

def get_flavorid(cpu, mem, disk):
    flavors_list = get_flavors_detail()['flavors']
    for i in range(len(flavors_list)):
        if ((cpu == flavors_list[i]["vcpus"]) and (mem == flavors_list[i]["ram"]) and (disk == flavors_list[i]["disk"])):
            return flavors_list[i]["id"]
    # print("SORRY，没有匹配的配置信息")

# print(len(get_flavors_detail()['flavors']))
# print(get_flavorid(1, 1, 1))
# print(get_flavors_detail()['flavors'][0]["ram"])
# print(get_flavors_detail()['flavors'][0]["disk"])


#删除所有的flavor
# for i in get_flavors_id_list():
#     delete_flavor(i)


"""
删除虚拟机
"""
def delete_vm(uuid):
    url = OS_AUTH_URL + ':8774/v2.1/servers/%s' %uuid
    headers['X-Auth-Token'] = get_token()
    result = requests.delete(url, headers=headers)
    return result


"""
虚拟机的属性：id，name，flavor(cpu, mem, disk)，hostname
"""

if __name__ == "__main__":
    # create_vm("vm5", "6614f4fa-f6f6-11e8-8398-1c1b0d5b7153")
    #虚拟机id
    # print(get_servers_detail_info()["servers"][0]['id'])
    # #虚拟机名字
    # print(get_servers_detail_info()["servers"][0]['name'])
    # #虚拟机flavor的id
    # print(get_servers_detail_info()["servers"][0]['flavor']['id'])
    # print(get_servers_detail_info()["servers"][0]['flavor'])
    # print(get_servers_detail_info()["servers"][1]['OS-EXT-SRV-ATTR:host'])

    # print(get_flavors_detail()['flavors'][0]["vcpus"])
    # print(get_flavors_detail()['flavors'][0]["ram"])
    # print(get_flavors_detail()['flavors'][0]["disk"])
    service()






