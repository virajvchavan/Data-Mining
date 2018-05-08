# just remember the logic for merging the clusters, everything else is easy.

def read_data():
	dataset = {}
	dataset['rows'] = ['a', 'b', 'c', 'd', 'e', 'f']
	dataset['mat']  = [
						[0,662,877,255,412,996],
						[662,0,295,468,268,400],
						[877,295,0,754,264,138],
						[255,468,754,0,219,869],
						[412,268,264,219,0,669],
						[996,400,138,869,669,0]
					  ]
	return dataset

def print_dataset(dataset, complete = False):
	print("\n", end="\t")
	for col in dataset['rows']:
		print(col, end='\t')
	if complete:
		for i in range(len(dataset['mat'])):
			print("\n" + str(dataset['rows'][i]), end="\t")
			for num in dataset['mat'][i]:
				print(num, end='\t')

		print('\n--------------------------------------------------------')

def find_position_of_min_distance(matrix):
	min_distance = 999999
	min_x = 0
	min_y = 0
	for x in range(len(matrix)):
		for y in range(len(matrix[x])):
			if(y >= x):
				continue
			if(matrix[x][y] < min_distance):
				min_distance = matrix[x][y]
				min_x = x
				min_y = y
	return [min_x, min_y]

def merge_clusters(dataset, min_position):
	matrix = dataset['mat']
	new_mat = []
	min_index_of_merged = min(min_position)
	max_index_of_merged = max(min_position)

	dataset['rows'][min_index_of_merged] += dataset['rows'][max_index_of_merged]
	del dataset['rows'][max_index_of_merged]

	# this here is crucial, remember this
	for x in range(len(matrix) - 1):
		# we go row-wise
		new_row = []
		for y in range(len(matrix) - 1):
			value = matrix[x][y]

			if(x == min_index_of_merged):
				value = min(value, matrix[max_index_of_merged][y])

			elif(y == min_index_of_merged):
				value = min(value, matrix[max_index_of_merged][x])

			new_row.append(value)
		new_mat.append(new_row)
	dataset['mat'] = new_mat
	return dataset

def main():
	dataset = read_data()
	while len(dataset['mat']) >= 1:
		print_dataset(dataset)
		min_position = find_position_of_min_distance(dataset['mat'])
		dataset = merge_clusters(dataset, min_position)

main()