def read_data():
	dataset = {}
	dataset['rows'] = ['a', 'b', 'c', 'd', 'e', 'f']
	dataset['cols'] = ['a', 'b', 'c', 'd', 'e', 'f']
	dataset['mat']  = [[0,662,877,255,412,996],
									[662,0,295,468,268,400],
									[877,295,0,754,264,138],
									[255,468,754,0,219,869],
									[412,268,264,219,0,669],
									[996,400,138,869,669,0]]
	return dataset

dataset = read_data()


print(dataset)