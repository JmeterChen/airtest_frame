# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-04-15


import subprocess

def aaa(*args):
	print(type(*args))
	b = map(lambda a: a+1, *args)
	return b


if __name__ == '__main__':
	# c = aaa()
	# print(list(c))
	# # a = 11, 22, 33
	# # print(type(a))

	simulator_process = 'ps -ef|grep "NemuPlayer"|grep -v grep|awk \'{print $2}\''
	back = subprocess.Popen(simulator_process, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	# print("back0----", back[0].decode())  # 注意需要进行解码操作，默认输出的是字节
	# print("back1----", back[1].decode())  # back是一个元祖，可以通过元祖取值的方式获取结果
	
	devices_data = back[0].decode()  # 获取模拟器进程号
	devices_list = devices_data.strip().split("\n")[1:]  # 获取模拟器进程号列表
	print(devices_list)