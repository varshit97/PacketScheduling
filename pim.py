#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

n = input()
inp = {}
for i in range(1, n + 1):
	k = []
	r = raw_input()
	r = r.strip().split(' ')
	for j in r:
		if j == '-':
			break
		k.append(int(j))
	inp[i] = k
# print inp
final = []
val = sum([len(i) for i in inp.values()])
# print val
count = 1
while val != 0:
	print 'Start of Round', count
	using = []
	needtomap = {}
	mapped = {}
	for i in inp.keys():
		needtomap[i] = 0
		mapped[i] = 0
		if len(inp[i]) != 0:
			needtomap[i] = 1
	iterCount = 1
	while 1:
		print 'Start of Iteration', iterCount
		cnt = 0
		for i in inp.keys():
			if needtomap[i] == mapped[i]:
				cnt += 1
			else:
				fl = 0
				for j in inp[i]:
					if j not in using:
						fl = 1
						break
				if fl == 0:
					cnt += 1

		if cnt == n:
			break

		revmap = {}
		for i in inp.keys():
			if mapped[i] != 1:
				for j in inp[i]:
					if j not in using:
						if j not in revmap.keys():
							temp = []
							temp.append(i)
							revmap[j] = temp
						else:
							revmap[j].append(i)
		ran = {}
		for i in revmap:
			k = random.choice(revmap[i])
			if k in ran.keys():
				ran[k].append(i)
			else:
				temp = []
				temp.append(i)
				ran[k] = temp
		for i in ran:
			k = random.choice(ran[i])
			mapped[i] = 1
			print i, '->', k
			temp = []
			temp.append(i)
			temp.append(k)
			final.append(temp)

			using.append(k)
			inp[i].remove(k)
		print 'End of Iteration', iterCount
		iterCount += 1
	val = sum([len(i) for i in inp.values()])
	print 'End of Round', count
	count += 1