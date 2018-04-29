import math
def read_dataset(filename):
	lines = open(filename).readlines()
	data = []
	for line in lines:
		data.append(list(map(float, line.split(','))))
	return data

def split_data(data, split_ratio):
	index = int(len(data) * split_ratio)
	return data[:index], data[index + 1: ]

def divide_by_class(train):
	data = {}
	for row in train:
		if row[-1] not in data:
			data[row[-1]] = []
		data[row[-1]].append(row)
	return data

def mean(values):
	return(sum(values)/float(len(values)))

def std(values):
	return 2

def get_summary(instances):
	summary =  [(mean(a), std(a)) for a in zip(*instances)]
	return summary[:-1]

def summarize_by_class(train):
	separated = divide_by_class(train)
	summaries = {}
	for class_value in separated:
		instances = separated[class_value]
		summaries[class_value] = get_summary(instances)
	return summaries

def classify():
	data =  read_dataset('diabetis.csv')
	split_ratio = 0.70
	train, test = split_data(data, split_ratio)
	summaries = summarize_by_class(train)
	print summaries

classify()

