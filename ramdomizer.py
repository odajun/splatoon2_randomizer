#!/usr/bin/python
# -*- coding: utf-8 -*-


import random

team_random = 0
stage_random = 0

def readFileTOList(path):
	list = []
	f = open(path,'r')
	for line in f:
		line = line.strip()
		if line.startswith('#'):
			continue
		if len(line) == 0:
			continue
		list.append(line)
	f.close()
	return list

rule_file = "./rule_list.txt"
rule_list = readFileTOList(rule_file)
print(random.choice(rule_list))

if stage_random != 0 :
	stage_file = "./stage_list.txt"
	stage_list = readFileTOList(stage_file)
	print(random.choice(stage_list))

member_file = "./member_list.txt"
member_list = readFileTOList(member_file)
random.shuffle(member_list)

wepon_type_list = []
shooter_file = "./shooter_file.txt"
shooter_list = readFileTOList(shooter_file)
wepon_type_list = wepon_type_list + shooter_list

charger_file = "./charger_file.txt"
charger_list = readFileTOList(charger_file)
wepon_type_list = wepon_type_list + charger_list

blaster_file = "./blaster_file.txt"
blaster_list = readFileTOList(blaster_file)
wepon_type_list = wepon_type_list + blaster_list

roller_file = "./roller_file.txt"
roller_list = readFileTOList(roller_file)
wepon_type_list = wepon_type_list + roller_list

inkbrush_file = "./inkbrush_file.txt"
inkbrush_list = readFileTOList(inkbrush_file)
wepon_type_list = wepon_type_list + inkbrush_list

slosher_file = "./slosher_file.txt"
slosher_list = readFileTOList(slosher_file)
wepon_type_list = wepon_type_list + slosher_list

splatling_file = "./splatling_file.txt"
splatling_list = readFileTOList(splatling_file)
wepon_type_list = wepon_type_list + splatling_list

manuver_file = "./manuver_file.txt"
manuver_list = readFileTOList(manuver_file)
wepon_type_list = wepon_type_list + manuver_list

shelter_file = "./shelter_file.txt"
shelter_list = readFileTOList(shelter_file)
wepon_type_list = wepon_type_list + shelter_list

wepon_free = "好きな武器を使うのです(=ω=)b"
wepon_type_list.append(wepon_free)


count = 1
alpha_list = []
bravo_list = []
watch_list = []

for member in member_list :
	if count > 8 :
		line = member + " : 観戦"
		watch_list.append(line)
	else :
		wepon = random.choice(wepon_type_list)
		line = member + " : " + wepon
		if count & 1 :
			alpha_list.append(line)
		else :
			bravo_list.append(line)

	count = count + 1

if team_random != 0 :
	print('')
	print "アルファチーム"

for i in alpha_list :
	print i

if team_random != 0 :
	print('')
	print "ブラボーチーム"
for i in bravo_list :
	print i 
print('')
if len(watch_list) > 0 :
	print "観戦"
	for i in watch_list :
		print i
