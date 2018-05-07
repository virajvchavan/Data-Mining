# https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
import math
from random import *
def read_dataset(filename):
	lines = open(filename).readlines()
	data = []
	for line in lines:
		data.append(list(map(float, line.split(','))))
	return data

def split_data(data, split_ratio):
	shuffle(data)
	index = int(len(data) * split_ratio)
	return data[:index], data[index + 1: ]

# divides the whole dataset according to what class they belong to
# returns { 1: [[a,c,d,1],[d,f,w,1],[f,w,r,1],...], 2: [[f,s,f,2],[v,e,s,2],[f,s,e,2],...] }
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
	avg = mean(values)
	var = 0
	for val in values:
		var += pow(val - avg, 2)
	std =  math.sqrt(var/(float(len(values) - 1)))
	if std == 0.0:
		std = 0.000001
	return std

# gets mean and std_deviation for each attribute
# the zip method gets all the values for each attribute in a single list
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

def get_probability(x, mean, std):
	e = math.exp(-(math.pow(x-mean, 2)/(2 * math.pow(std, 2))))
	return (1 / (math.sqrt(2*math.pi) * std)) * e

def get_class_probabs(summaries, row):
	class_probabs = {}
	for class_name, class_summaries in summaries.items():
		class_probabs[class_name] = 1
		for i in range(len(class_summaries)):
			x  = row[i]
			mean, std = class_summaries[i]
			class_probabs[class_name] *= get_probability(x, mean, std)
	return class_probabs

# for a row in test data
def predict(summaries, row):
	# summaries = { class1: (mean, std), class2: (mean, std) }
	class_probabs = get_class_probabs(summaries, row)
	probab = -1
	predicted_class = None
	for class_name, class_probab in class_probabs.items():
		if predicted_class == None or probab < class_probab:
			probab = class_probabs[class_name]
			predicted_class = class_name
	return predicted_class

def get_predictions(summaries, test):
	predictions = []
	for row in test:
		predictions.append(predict(summaries, row))
	return predictions

def get_accuracy(predictions, test):
	correct = 0
	for i in range(len(test)):
		if test[i][-1] == predictions[i]:
			correct += 1
	return float(correct)/float(len(test))

def classify(filename):
	data =  read_dataset(filename)
	split_ratio = 0.60
	train, test = split_data(data, split_ratio)
	summaries = summarize_by_class(train)
	predictions = get_predictions(summaries, test)
	print(predictions)
	accuracy = get_accuracy(predictions, test)
	print(accuracy)

classify('glass_data.csv')