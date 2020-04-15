# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-03-31


import subprocess, time, os


def get_cmd_data(command, t=None):
	"""
	:param command:         需要在命令窗口输入命令， eg：ls -la
	:param t:               输入命令后，命令行窗口返回数据结果；
	:return:
	"""
	# 拿到命令行窗口返回的命令结果(bytes类型)
	back = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	devices_data = back[0].decode().strip()
	if not t:
		return devices_data
	elif devices_data and t == list:
		return devices_data.split("\n")


def get_devicesList():
	"""
	:return:    链接的设备列表,没有则返回空列表
	"""
	command = "adb devices -l"
	devices_data = get_cmd_data(command)
	devices_list = devices_data.strip().split("\n")[1:]  # 获取链接设备列表
	return devices_list


def connect_devices(devices):
	"""
	:param devices:  设备名称
	:return:
	"""
	if type(devices) == str:
		command = 'adb connect %s' % devices
		# 执行链接设备
		os.popen(command)
	else:
		# TODO 需要去补充链接多个设备的情况
		pass


def check_simulator(service):
	"""
	:param service:     传入模拟器名称，eg：NemuPlayer/NoxAppPlayer
	:return:            返回传入模拟器对应的进程ID
	"""
	simulator_process = 'ps -ef|grep %s|grep -v grep|awk \'{print $2}\'' % service
	data = get_cmd_data(simulator_process, list)
	return data
	

def start_simulator():
	s = get_devicesList()
	print(s)
	if not s:  # 如果没有连接设备，我们默认打开夜神模拟器进行测试
		# Mac上启动模拟器命令
		command = "open /Applications/NemuPlayer.app/Contents/MacOS/NemuInstaller.app"
		os.popen(command)
		time.sleep(10)
		connect_devices('127.0.0.1')
		if check_simulator('NemuPlayer'):
			return True
	else:
		return True
		

if __name__ == '__main__':
	# x = get_devicesList()
	# print(x)
	# y = start_simulator()
	# print(y)
	# c = 'ps -ef|grep "NemuPlayer"|grep -v grep|awk \'{print $2}\''
	# print(get_cmd_data(c, list))
	# print(get_devicesList())
	# cmd = 'ps -ef|grep "NemuPlayer"|grep -v grep|awk \'{print $2}\''
	# print(get_cmd_data(cmd))
	# print(check_simulator("NoxAppPlayer"))
	# print(type(check_simulator("NemuPlayer")))
	# print(get_devicesList())
	print(start_simulator())