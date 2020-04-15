# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2020-04-15


a = [1, 2, 3, 4, 5, 5]
m = {}
for i in a:
	print(m.get(i))
	m[i] = m.get(i, 0) + 1
	

print(m)

