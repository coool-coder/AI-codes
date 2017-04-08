import numpy as np
from numpy import *
from KNNC import *
import collections as cl


def MeanError(labels, actual_labels):
	labels = np.asarray(labels)
	actual_labels = np.asarray(actual_labels)
	error_vector = 0.5*(actual_labels - labels)**2
	error = np.mean(error_vector)
	return error


def main():
	
	k = int(input())	
	
	Training_Data = loadtxt("occupancy_data/datatraining.txt", delimiter="," , skiprows = 1, usecols=(2,3,4,5,6,7))
	Test_Data = loadtxt("occupancy_data/datatest2.txt", delimiter="," , skiprows = 1, usecols=(2,3,4,5,6,7))
	
	score = Distance(Test_Data,Training_Data)
	print score
	idx = np.empty([0,score.shape[1]], dtype=int)	
	for j in range(0,score.shape[0]):
		# import pdb; pdb.set_trace()
		ind = np.argpartition(score[j],3)
		idx = np.vstack((idx,ind))
		
	arr = idx[:,0:k]
	print arr

	m,_ = arr.shape
	labels = list()

	for l in range(m):
		temp = []
		# import pdb; pdb.set_trace()
		for j in range(k):  #storing the corresponding labels
			temp.append(Training_Data[arr[l][j],5])
		count = cl.Counter(temp)
		if count[0] > count[1]:
			labels.append(0)
		else:
			labels.append(1)
			
	
	actual_labels = Test_Data[:,5].tolist()

	classified=0
	missclassified=0
	for i in range(len(actual_labels)):
		if actual_labels[i] == labels[i]:
			classified+=1	
	accuracy = float(classified)/float(len(actual_labels))

	print "accurracy:", accuracy*100

	Error = MeanError(labels, actual_labels)
	print ("Error: ", Error)

if __name__=="__main__":
	main()
