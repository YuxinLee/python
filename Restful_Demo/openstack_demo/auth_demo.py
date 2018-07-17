#coding=utf-8

import requests
import json

OS_AUTH_URL="http://192.168.246.130"
body = '''
{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "id": "ad593d166aed4f268d5a93193fa4df9a",
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

headers={}
headers['Content-Type'] = 'application/json'
headers['Accept'] = '*/*'


def get_token():
    get_token_url=OS_AUTH_URL+':35357/v3/auth/tokens'
    #result=requests.post(get_token_url,headers=headers,data=json.dumps(body)).headers['X-Subject-Token']
    result = requests.post(get_token_url,headers=headers,data=body).headers['X-Subject-Token']
    return result



def user_list():
    user_list_url=OS_AUTH_URL+':35357/v3/users'
    headers['X-Auth-Token']=get_token()
    result=requests.get(user_list_url,headers=headers).json()
    return (result)
#print user_list()['users'][1]['links']

def images_info_list():
    images_list_url=OS_AUTH_URL+':9292/v2/images'
    headers['X-Auth-Token']=get_token()
    result=requests.get(images_list_url,headers=headers).json()
    return result

#print images_info_list()

def images_name_list():
    images_name_list = []
    length = len(images_info_list()['images'])
    for i in range(length):
        images_name_list.append(images_info_list()['images'][i]['name'])
    return images_name_list

#print images_name_list()

def servers_info_list():
    computes_list_url = OS_AUTH_URL + ':8774/v2.1/servers'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(computes_list_url, headers=headers).json()
    return (result)

#print servers_info_list()

def servers_name_list():
    servers_name_list = []
    length = len(servers_info_list()['servers'])
    for i in range(length):
        servers_name_list.append(servers_info_list()['servers'][i]['name'])
    return servers_name_list

#print servers_name_list()

def flavors_info_list():
    flavors_list_url = OS_AUTH_URL + ':8774/v2.1/flavors'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(flavors_list_url, headers=headers).json()
    return result

#print flavors_info_list()

def flavors_name_list():
    flavors_name_list = []
    length = len(flavors_info_list()['flavors'])
    for i in range(length):
        flavors_name_list.append(flavors_info_list()['flavors'][i]['name'])
    return flavors_name_list

#print flavors_name_list()

def security_groups_info_list():
    security_group_list_url = OS_AUTH_URL + ':8774/v2.1/os-security-groups'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(security_group_list_url, headers=headers).json()
    return result

#print security_group_info_list()['security_groups'][0]['name']
#print len(security_groups_info_list()['security_groups'])

def security_groups_name_list():
    security_groups_name_list = []
    length = len(security_groups_info_list()['security_groups'])
    for i in range(length):
        security_groups_name_list.append(security_groups_info_list()['security_groups'][i]['name'])
    return security_groups_name_list

#print security_groups_name_list()

def networks_info_list():
    network_list_url = OS_AUTH_URL + ':9696/v2.0/networks'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(network_list_url, headers=headers).json()
    return result

#print networks_info_list()['networks'][0]['id']

def networks_name_list():
    networks_name_list = []
    length = len(networks_info_list()['networks'])
    for i in range(length):
        networks_name_list.append(networks_info_list()['networks'][i]['name'])
    return networks_name_list

# print networks_name_list()

def networks_id_list():
    networks_id_list = []
    length = len(networks_info_list()['networks'])
    for i in range(length):
        networks_id_list.append(networks_info_list()['networks'][i]['id'])
    return networks_id_list

#print networks_id_list()

def subnets_info_list():
    subnet_list_url = OS_AUTH_URL + ':9696/v2.0/subnets'
    headers['X-Auth-Token'] = get_token()
    result = requests.get(subnet_list_url, headers=headers).json()
    return (result)

#print subnets_info_list()

def subnets_name_list():
    subnets_name_list = []
    length = len(subnets_info_list()['subnets'])
    for i in range(length):
        subnets_name_list.append(subnets_info_list()['subnets'][i]['name'])
    return subnets_name_list

#print subnets_name_list()

def subnets_id_list():
    subnets_id_list = []
    length = len(subnets_info_list()['subnets'])
    for i in range(length):
        subnets_id_list.append(subnets_info_list()['subnets'][i]['id'])
    return subnets_id_list

#print subnets_id_list()

def create_vm():
    headers['X-Auth-Token'] = get_token()
    create_vm_url = OS_AUTH_URL + ':8774/v2.1/servers'
    create_vm_body='''
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
    print result.json()

create_vm()

