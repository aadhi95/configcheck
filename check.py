separator = "="
key = []
key1 = []
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
if len(set(key).intersection(key1))==len(key):
	print(1)
else:
	print(0)
