import math

def read_dataset(filename):
	data = {}
	lines = open(filename).readlines()
	data['headers'] = lines[0].split(',')
	data['no_of_tuples'] = len(lines) - 1
	for h in data['headers']:
		data[h] = []
	# so far:  {'outlook': [], 'temp': [], 'count_tuples': 14, 'humidity': [], 'headers': ['outlook', 'temp', 'humidity', 'windy', 'play\n'], 'windy': [], 'play\n': []}	
	for line in lines[1:]:
		line = line.split(',')
		for i in range(len(data['headers'])):
			data[data['headers'][i]].append(line[i])
	return data

data = read_dataset('tennis.csv')
print data