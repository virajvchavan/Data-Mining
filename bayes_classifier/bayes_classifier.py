dataset = [	[6,148,72,1],
						[1,85,66,0],
						[8,183,64,1],
						[1,89,66,0],
						[0,137,40,1],
						[5,116,74,0],
						[3,78,50,1]
					]

def get_transpose(dataset):
	return 	[	[6,1,8,1,0,5,3],
						[148,85,183,89,137,116,78],
						[72,66,64,66,40,74,50],
						[1,0,1,0,1,0,1]
					]

def get_class_probabilities(class_values):
	unique_elements =  list(set(class_values))
	class_counts = [0 for _ in unique_elements]
	for c in class_values:
		for i, ele in enumerate(unique_elements):
			if c == ele:
				class_counts[i] += 1

	return [float(count)/len(class_values) for count in class_counts]
datasetT = get_transpose(dataset)

class_probabilties = get_class_probabilities(datasetT[-1])

print class_probabilties
