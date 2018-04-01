def read_data():
	dataset = {}
	dataset['rows'] = ['a', 'b', 'c', 'd', 'e', 'f']
	dataset['cols'] = ['a', 'b', 'c', 'd', 'e', 'f']
	dataset['mat']  = [
											[0,662,877,255,412,996],
											[662,0,295,468,268,400],
											[877,295,0,754,264,138],
											[255,468,754,0,219,869],
											[412,268,264,219,0,669],
											[996,400,138,869,669,0]
										]
	return dataset

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
	for x in range(len(matrix) - 1):
		new_row = []
		for y in range(len(matrix) - 1):
			value = matrix[x][y]
			if(x == min(min_position)):
				value = min(value, matrix[max(min_position)][y])
			elif(y == max(min_position)):
				value = min(value, mat[max(min_position)][x])
			new_row.append(value)
		new_mat.append(new_row)
	return new_mat


dataset = read_data()
print(dataset)

min_position = find_position_of_min_distance(dataset['mat'])
dataset = merge_clusters(dataset, min_position)

print(dataset)