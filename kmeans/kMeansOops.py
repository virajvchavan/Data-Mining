import pandas as pd
import math
import copy
class Cluster:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.element = [[x,y]]

	def getcenter(self):
		return self.x,self.y

	def addelement(self,x,y):
		tmp = [x,y]
		self.element.append(tmp)

	def removeelement(self,x,y):
		tmp = [x,y]
		self.element.remove(tmp)

	def cntelement(self):
		return len(self.element)

	def find(self,x,y):
		tmp = [x,y]
		return (tmp in self.element)

	def distance(self,x2,y2):
		return math.sqrt((x2-self.x)**2 + (y2-self.y)**2)

	def mean(self):
		if(self.cntelement()!=0):
			x ,y = 0, 0
			for i in self.element:
				x += i[0]
				y += i[1]
			self.x = x/self.cntelement() 
			self.y = y/self.cntelement()
	def display(self):
		print("\nCluster content ")
		for i in self.element:
			print(i,end=" ")

	def __eq__(self,other):
		return self.__dict__ == other.__dict__

def display(clusters):
	for i in range(k):
		print(clusters[i].getcenter())


def calculatemean(clusters,xdata,ydata,k):
	for i in range(len(xdata)):
		dist = 99999999999999
		cl = -1
		for j in range(k):
			di = clusters[j].distance(xdata[i],ydata[i]) 
			if(di < dist):
				dist = di
				cl = j
		for j in range(k):
			if(clusters[j].find(xdata[i],ydata[i])):
				clusters[j].removeelement(xdata[i],ydata[i])
			clusters[j].mean()
		clusters[cl].addelement(xdata[i],ydata[i])
		clusters[cl].mean()
	return clusters

if __name__ == "__main__":
	k = int(input("Enter no of clusters to form : "))
	itr = int(input("Enter no of iteration to perform : "))
	data = pd.read_csv("file.csv")
	xdata = list(data.iloc[: ,0])
	ydata = list(data.iloc[: ,1])
	clusters = []

	if(k>=len(xdata)):
		print("value of k should be less than data length - 1")

	else:
		for i in range(k):
			clus = Cluster(xdata[i],ydata[i])
			clusters.append(clus)

		tmp = copy.deepcopy(clusters)
		for i in range(itr):
			clusters = calculatemean(clusters,xdata,ydata,k)
			if(tmp == clusters):
				print("It required ",i," iterations to calculate clusters")
				break
			tmp = copy.deepcopy(clusters)
			
		display(clusters)
		for i in range(k):
			clusters[i].display()




	



