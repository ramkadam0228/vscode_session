import configparser
import os
def  getconfig():

    config_1 = configparser.ConfigParser()
    config_1.read('properties.ini')
    # path = '/'.join((os.path.abspath('python_oops\requests\resources').replace('\\', '/')).split('/')[:-1])
    # config.read(os.path.join(path, 'properties.ini'))

    return config_1