# -*- encoding=UTF-8 -*-
from flask_script import Manager
from flask_demo.service import app

#可以通过输入脚本 python manager.py runserver来运行app
manager = Manager(app)

#python flask_script.py hello -n --name=test
@manager.option('-n',  '--name', dest='name', default='nowcoder')
def hello(name):
    print ('hello', name)

#python flask_script.py
@manager.command
def initialize_database():
    'initialize database'
    print ('database ...')

if __name__ == '__main__':
    manager.run()