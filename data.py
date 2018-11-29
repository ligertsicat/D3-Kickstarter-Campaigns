print("hello")

import csv
import json

d = dict()

with open('data.csv', 'r', encoding="utf8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		key = row[2]+"---celestinaisadorable---"+row[3]
		if key in d:
			d[key] += 1
		else:
			d[key] = 1


success = dict()
failed = dict()

with open('data.csv', 'r', encoding="utf8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		key = row[2]+"---celestinaisadorable---"+row[3]
		if row[5] == "successful":
			if key in success:
				success[key] += 1
			else:
				success[key] = 1

with open('data.csv', 'r', encoding="utf8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		key = row[2]+"---celestinaisadorable---"+row[3]
		if row[5] == "failed":
			if key in failed:
				failed[key] += 1
			else:
				failed[key] = 1

treemapJson = dict()

for key in d:
	print (key.split("---celestinaisadorable---"), d[key])
	treemapJson["key"] = ""
	treemapJson["subcategory"] = key[1]
	treemapJson["category"] = key[2]
	treemapJson["value"] = d[key]

f = open("treemap.json", "w")
f.write('[\n')
for key in d:
	f.write('{\n')
	f.write('"key": "' + key.split("---celestinaisadorable---")[1] + '",\n')
	f.write('"subcategory": "' + key.split("---celestinaisadorable---")[1] + '",\n')
	f.write('"category": "' + key.split("---celestinaisadorable---")[0] + '",\n')
	f.write('"value": ' + str(d[key]) + '\n')
	f.write('},\n')
f.write(']\n')
'''
for key in failed:
	print (key, success[key] / (failed[key]+success[key])) 
'''
'''
length = dict()
length_num = dict()

with open('cleaned_USA_Final.csv', 'r', encoding="utf8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		key = row[3]+row[4]
		if key in length:
			length[key] += len(row[2])
			length_num[key] += 1
		else:
			length[key] = len(row[2])
			length_num[key] = 1

for key in length:
	print (length[key]/length_num[key], key)



goal = dict()
goal_num = dict()

first = 1

with open('cleaned_USA_Final.csv', 'r', encoding="utf8") as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:

		if first == 1:
			first = 0
			continue

		key = row[3]+row[4]
		if key in goal:
			goal[key] += float(row[7])
			goal_num[key] += 1
		else:
			goal[key] = float(row[7])
			goal_num[key] = 1


for key in goal:
	print (goal[key]/goal_num[key], key)
	'''