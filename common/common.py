import datetime
import time
import config
import hashlib
from gevent import getcurrent
import random

rand_string = 'qwertyuiopasdfghjklzxcvbnm1234567890'


# 时间戳转2018-01-01 8:00:00
def time_to_str(times=time.time()):
    date_array = datetime.datetime.utcfromtimestamp(times + (8 * 3600))
    return date_array.strftime("%Y-%m-%d %H:%M:%S")


def get_md5(string):
    md5 = hashlib.md5(string.encode('ascii')).hexdigest()
    return md5
    # 计算md5校验
    # 这里python作为一个弱类型语言的坑就出现了
    # 竟然传入值需要解码成ascii


def get_file_md5(binary):
    '''
    文件md5转换
    :param binary: 
    :return: 
    '''
    md5 = hashlib.md5().hexdigest()
    return md5


def get_event_id(data=None):
    id_string = str(id(getcurrent()))
    res = ''
    for i in id_string:
        res += random.choice(rand_string)

    res += id_string
    res += str(time.time())
    return get_md5(res)
    # 获得事件id编码

