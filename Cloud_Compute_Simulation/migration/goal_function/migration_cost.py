#coding=utf-8

from migration.migration_VMDM import algorithm_VMDM

def get_migration_cost():
    return algorithm_VMDM.get_total_migration_cost()