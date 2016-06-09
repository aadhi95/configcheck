import os
import sys
separator = "="
key = []
key1 = []
os.system('wget https://github.com/aadhi95/configcheck/raw/master/service.properties')
os.system('wget https://github.com/aadhi95/configcheck/raw/master/reference.properties')
with open('service.properties') as f:
	for line in f:
		if separator in line:
			name, value = line.split(separator, 1)
			key.append(name)
with open('reference.properties') as f:
	for line in f:
		if separator in line:
			name, value = line.split(separator, 1)
			key1.append(name)

if len(set(key).intersection(set(key1)))==len(set(key)):
	print("matches")
else:
	sys.exit(-1)
os.system('rm service.properties');
os.system('rm reference.properties')
