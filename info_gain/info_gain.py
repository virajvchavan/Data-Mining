# data should be categorical, not numerical
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

def p_log_p(p, q):
	if p == q:
		return 1
	elif p == 0 and q == 0:
		return 0
	return (p/q) * math.log(p/q, 2)

# calc info_gain for one attribute at a time
def info_gain(data, attribute):
	class_attr = data['headers'][-1]
	unique_attr_values = set(data[attribute])
	unique_class_attr_values = set(data[class_attr])

	# The main steps: 
	# step 1: I(information) = ( p * log(p)  for each unique value of 'attribute' )
	# step 2: E = sum of ( I * (count for this value of attr/data['no_of_tuples']) for each unique value of 'attribute')
	# step 3: InfoGain = E(class_attri) - E

	# To achieve these steps, we need to store the counts for each attribute values in a great way
	count_hash = {}
	# initializing...
	for val_of_attr in unique_attr_values:
		count_hash[val_of_attr] = {}
		count_hash[val_of_attr]['total'] = 0
		for val_of_class_attr in unique_class_attr_values:
			count_hash[val_of_attr][val_of_class_attr] = 0

	# storing counts...
	# {'mild': {'yes\n': 4, 'no\n': 2, 'total': 6}, 'hot': {'yes\n': 2, 'no\n': 1, 'total': 3}, 'cool': {'yes\n': 3, 'no\n': 1, 'total': 4}}	
	for i in range(0, data['no_of_tuples']):
		attr_val = data[attribute][i]
		class_attr_val = data[class_attr][i]
		count_hash[attr_val][class_attr_val] += 1
		count_hash[attr_val]['total'] += 1
	
	# now calculate the real shit
	entropy = 0
	for attr in unique_attr_values:
		info = 0
		for class_attr_val in unique_class_attr_values:
			info += p_log_p(count_hash[attr][class_attr_val], count_hash[attr]['total'])
		entropy += (info * (count_hash[attr]['total']/len(data[class_attr])))

	main_entropy = 0
	for attr in unique_class_attr_values:
		main_entropy += p_log_p(data[class_attr].count(attr), len(data[class_attr]))

	return (entropy - main_entropy)

data = read_dataset('tennis.csv')
# print data
print("Temperature: \t", info_gain(data, 'temp'))
print("Humidity: \t", info_gain(data, 'humidity'))
print("Windy: \t\t", info_gain(data, 'windy'))