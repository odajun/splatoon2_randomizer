#!/usr/bin/python
# -*- coding: utf-8 -*-


import random
import discord
import sys
from configparser import ConfigParser

team_random = 0
stage_random = 0
debug_mode = False
watcher_on = False
wepon_random_num = [1,2]

config = ConfigParser()
config.read('./randomizer.ini')

def readFileToList(path):
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

def readFileToWeponList(path):
	list = []
	f = open(path,'r')
	for line in f:
		line = line.strip()
		if line.startswith('#'):
			continue
		if len(line) == 0:
			continue
		list.append(line.split(","))
	f.close()
	return list

def run_randomizer(member_list):
    text = []
    text.append(random.choice(rule_list))

    if stage_random != 0 :
	    text.append(random.choice(stage_list))

    random.shuffle(member_list)

    count = 1
    alpha_list = []
    bravo_list = []
    watch_list = []
    
    for member in member_list :
        if watcher_on :
            if count > 8 :
                line = member + " : 観戦"
                watch_list.append(line)
                count = count + 1
                continue
    
        wepon1 = random.choice(wepon_type_list)
        wepon2 = random.choice(wepon_type_list)
        tmp = random.choice(wepon_random_num)
        if tmp & 1 : 
            line = member + " : " + wepon1[0]
        else :
            line = member + " : " + wepon1[1]
            line = line + " or " + wepon2[1]
        if count & 1 :
            alpha_list.append(line)
        else :
            bravo_list.append(line)
        count = count + 1
    
    if team_random != 0 :
        text.append("アルファチーム")
    
    for i in alpha_list :
        text.append(i)
    
    if team_random != 0 :
        text.append("ブラボーチーム")
    for i in bravo_list :
        text.append(i)
    
    if len(watch_list) > 0 :
        text.append("観戦")
        for i in watch_list :
            text.append(i)
    
    text = '\n'.join(text) 
    return text

rule_file = "./rule_list.txt"
rule_list = readFileToList(rule_file)

stage_file = "./stage_list.txt"
stage_list = readFileToList(stage_file)

wepon_type_list = []
shooter_file = "./shooter_file.txt"
shooter_list = readFileToWeponList(shooter_file)
wepon_type_list = wepon_type_list + shooter_list

charger_file = "./charger_file.txt"
charger_list = readFileToWeponList(charger_file)
wepon_type_list = wepon_type_list + charger_list

blaster_file = "./blaster_file.txt"
blaster_list = readFileToWeponList(blaster_file)
wepon_type_list = wepon_type_list + blaster_list

roller_file = "./roller_file.txt"
roller_list = readFileToWeponList(roller_file)
wepon_type_list = wepon_type_list + roller_list

inkbrush_file = "./inkbrush_file.txt"
inkbrush_list = readFileToWeponList(inkbrush_file)
wepon_type_list = wepon_type_list + inkbrush_list

slosher_file = "./slosher_file.txt"
slosher_list = readFileToWeponList(slosher_file)
wepon_type_list = wepon_type_list + slosher_list

splatling_file = "./splatling_file.txt"
splatling_list = readFileToWeponList(splatling_file)
wepon_type_list = wepon_type_list + splatling_list

manuver_file = "./manuver_file.txt"
manuver_list = readFileToWeponList(manuver_file)
wepon_type_list = wepon_type_list + manuver_list

shelter_file = "./shelter_file.txt"
shelter_list = readFileToWeponList(shelter_file)
wepon_type_list = wepon_type_list + shelter_list

wepon_free = ["好きな武器を使うのです","Free"]
wepon_type_list.append(wepon_free)

akane_happy_file = "./happy.txt"
akane_happy_list = readFileToList(akane_happy_file)

akane_normal_file = "./normal.txt"
akane_normal_list = readFileToList(akane_normal_file)

akane_bad_file = "./bad.txt"
akane_bad_list = readFileToList(akane_bad_file)

if debug_mode :
    member_file = "./member_list.txt"
    member_list = readFileToList(member_file)
    
    text = run_randomizer(member_list)
    print(text)
    sys.exit(0)

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    text = "おいっす!あけましておめでとう。今年もよろしく。"
    server = client.get_server("421886050978365450")
# general text chanel
#text_channel = server.get_channel("421886050978365453")
# akane_chan text chanel
    text_channel = server.get_channel("518472075791564811")
#general = client.get_channel(config['channel_id']['general'])
#hard_coded_channel = discord.Object(id=config['channel_id']['general'])
#yield from client.send_message(hard_coded_channel, text)
#await client.send_message(text_channel, text)
    await client.send_message(text_channel, text)

@client.event
async def on_message(message):
    if message.content.startswith('/debug'):
        reply = 'これはテストやから無視したってな'
        await client.send_message(message.channel, reply)
    if message.content.startswith('/茜ちゃん') or message.content.startswith('一番いいのを頼む') or message.content.startswith('/buki'):
        general = client.get_channel(config['channel_id']['general'])
        alpha = client.get_channel(config['channel_id']['baitomin'])
        bravo = client.get_channel(config['channel_id']['fesmin'])
    
        member_list = []
        for member in general.voice_members :
            member_list.append(member.name)
        for member in alpha.voice_members :
            member_list.append(member.name)
        for member in bravo.voice_members :
            member_list.append(member.name)

        if len(member_list) > 0 :
            text = run_randomizer(member_list)
        else :
            text = "今誰もおらんやないの。"
        await client.send_message(message.channel, text)

    if message.content.startswith('茜ちゃん勝ったで') or message.content.startswith('/win') or message.content.startswith('自分がんばった') :
        user = message.author.name
        reply_list = []
        reply_list.extend(akane_happy_list)
        reply_list.extend(akane_normal_list)
        akane_text = user + " " + random.choice(reply_list)
        await client.send_message(message.channel, akane_text)

    if message.content.startswith('茜ちゃん負けたわ') or message.content.startswith('/lose') :
        user = message.author.name
        reply_list = []
        reply_list.extend(akane_bad_list)
        reply_list.extend(akane_normal_list)
        akane_text = user + " " + random.choice(reply_list)
        await client.send_message(message.channel, akane_text)

    if message.content.startswith('茜ちゃんおやすみ'): 
        user = message.author.name
        akane_text = user + " " + "おやすみ。ええ夢見るんやで。"
        await client.send_message(message.channel, akane_text)

    if message.content.startswith('茜ちゃんかわいい') or message.content.startswith('茜ちゃんpretty'): 
        text = "せやろ？"
        await client.send_message(message.channel, text)

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run(config['access_token']['token'])

