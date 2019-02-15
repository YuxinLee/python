#coding=utf-8

import pymysql
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:passw0rd@192.168.241.144:3306/cloud_compute_simulation')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

class Result(Base):
    # 表的名字:
    __tablename__ = 'result_DT'

    result_id = Column(String(50), primary_key=True)
    timestamps = Column(Integer)
    power_consumption = Column(Float)
    bandwidth_consumption = Column(Float)
    active_host_num = Column(Integer)
    migration_cost = Column(Float)

def create_table_result():
    # 连接数据库mysql
    db = pymysql.connect("192.168.241.144", "root", "passw0rd", "cloud_compute_simulation", charset='utf8')
    cursor = db.cursor()

    # 在数据库mysql中创建主机host的数据表
    cursor.execute("DROP TABLE IF EXISTS result_DT")
    create_result_table_sql = """CREATE TABLE result_DT (
             result_id varchar(50) PRIMARY KEY,
             timestamps  int NOT NULL,
             power_consumption  float NOT NULL,
             bandwidth_consumption  float NOT NULL,
             active_host_num int NOT NULL,
             migration_cost  float NOT NULL
             )"""
    cursor.execute(create_result_table_sql)
    cursor.close()

def add_result_data(result):
    session = DBSession()
    contents = Result(result_id=result.result_id, timestamps=result.timestamps, power_consumption=result.power_consumption,
                      bandwidth_consumption=result.bandwidth_consumption, active_host_num = result.active_host_num,
                      migration_cost=result.migration_cost)
    session.add(contents)
    session.commit()
    session.close()

def get_result_list():
    session = DBSession()
    results = session.query(Result).all()
    session.close()
    return results

# def get_vm_number_list():
#     vm_number_list = []
#     result_list = get_result_list()
#     for i in range(len(result_list)):
#         vm_number_list.append(result_list[i].vm_number)
#     return vm_number_list

def get_power_consumption_list():
    energy_consumption_list = []
    result_list = get_result_list()
    for i in range(len(result_list)):
        energy_consumption_list.append(result_list[i].power_consumption)
    return energy_consumption_list

def get_bandwidth_consumption_list():
    bandwidth_consumption_list = []
    result_list = get_result_list()
    for i in range(len(result_list)):
        bandwidth_consumption_list.append(result_list[i].bandwidth_consumption)
    return bandwidth_consumption_list

def get_active_host_num_list():
    active_host_num_list = []
    result_list = get_result_list()
    for i in range(len(result_list)):
        active_host_num_list.append(result_list[i].active_host_num)
    return active_host_num_list

def get_timestamps_list():
    timestamps_list = []
    result_list = get_result_list()
    for i in range(len(result_list)):
        timestamps_list.append(result_list[i].timestamps)
    return timestamps_list

def get_migration_cost_list():
    migration_cost_list = []
    result_list = get_result_list()
    for i in range(len(result_list)):
        migration_cost_list.append(result_list[i].migration_cost)
    return migration_cost_list