#3 fold -> 2714-2714-2715
#Temperature - 1
#Humidity - 2
#Light - 3
#CO2 - 4
#HumidityRatio - 5
#Occupancy - 6
#Label - 7
#wi = (dk -di ) / (dk -d1)
#-------------------------------------------------------

import numpy as np
import collections as cl
from numpy import *


def Weight(score):
	weight_mat = score.copy()
	for i in range(score.shape[0]):
		dk = score[i,-1]
		d1 = score[i,0]
		for j in range(score.shape[1]):
			weight_mat[i,j] = float(dk - score[i,j])/float(dk - d1)

	return weight_mat

# Finding error for particular data set
def FindError(labels, actual_labels):
	w,h = labels.shape
	error = np.empty([1,h])
	# for i in range(h):
	# 	# import pdb; pdb.set_trace()
	# 	temp = labels[:,i]
	# 	error_vector = 0.5*(actual_labels - temp)**2  # 1/2*(yk - tk)^2
	# 	error[:,i] = np.mean(error_vector)
	
	for i in range(h):	
		missclassified=	0
		temp = labels[:,i]
		for j in range(w):
			if actual_labels[j] != temp[j]:
				missclassified+=1	
		temp_error = float(missclassified)/float(actual_labels.shape[0])
		error[:,i] = temp_error
	return error

# Computing Euclidean Distance to find the closeness
def Distance(X, Y):
	m,_ = X.shape
	l,_ = Y.shape
	score_mat = np.empty([m,l])
	for i in range(0, m):
		for j in range(0, l):
			dist = X[i] - Y[j]
			dist = dist**2
			_sum_ = sum(dist)
			euclidian_dist = np.sqrt(_sum_)
			score_mat[i,j] = euclidian_dist
	
	return score_mat
#-------------------------------------------------------


def ModCrossValidation(Data):
	w,h = Data.shape
	d1 = Data[0:2714,:]
	d2 = Data[2714:2*2714,:]
	d3 = Data[2*2714: 3*2714+1,:]
	
	Error_Mat = np.empty([0,10])
	for i in range(3):
		if i==0:
			validation_set = d1
			Training_set = np.vstack((d2, d3))

		elif i==1:
			validation_set = d2
			Training_set = np.vstack((d1, d3))

		elif i==2:
			validation_set = d3
			Training_set = np.vstack((d1, d2))
		print("i:", i)
		score = Distance(validation_set, Training_set)
		print("score: ")
		print(score)

		weight = Weight(score)
		
		m,n  = score.shape

		# storing the indexes of score_mat(row wise) in ascending order of the distances
		# idx[i][j] -> Tells the corresponding ith row in the Training_set with which the comparison done with 
		# jth data in the validation_set
		idx = np.empty([0,n], dtype=int)
		
		for j in range(0,m):
			# import pdb; pdb.set_trace()
			ind = np.argpartition(score[j],3)
			idx = np.vstack((idx,ind))
		
		print "idx:", '\n', idx
		actual_labels = validation_set[:,5]
		labels = np.empty([m,0])
		clone = np.zeros((m,1))
		# import pdb; pdb.set_trace()
		print "Training_set:"
		print Training_set 
		for k in range(1,20,2):
			arr = idx[:,0:k]
			m,_ = arr.shape
			out = np.empty([m,k])
			print "k:", k
			for l in range(m):
				temp = []
				# import pdb; pdb.set_trace()
				for j in range(k):  #storing the corresponding labels
					temp.append(Training_set[arr[l][j],5])
				w1=w0=0
				for l in range(0,k):
					if temp[l]==1:
						w1 = w1 + weight[l,j] 
					else:
						w0 = w0 + weight[l,j] 
				# count = cl.Counter(temp)
				if w0 > w1:
					clone[l][0] = 0
				else:
					clone[l][0] = 1
			labels = np.hstack((labels, clone))
		
		temp_error = FindError(labels, actual_labels)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																										
		Error_Mat = np.vstack((Error_Mat,temp_error))

	np.savetxt("Mod_Error_Mat.txt", Error_Mat)
	
	#computing std deviation of Error_mat for each k value
	std_dev = [np.std(Error_Mat[:,i]) for i in range(Error_Mat.shape[0])]


	Result = np.mean(Error_Mat,0)
	print ("Result:")
	print(Result)
		

	index = np.argmin(Result)
	k_suitable = 2*index + 1
	print("k:", k_suitable)

	return k_suitable

# 3-Fold Cross-Validation Implementation
def CrossValidation(Data):
	w,h = Data.shape
	d1 = Data[0:2714,:]
	d2 = Data[2714:2*2714,:]
	d3 = Data[2*2714: 3*2714+1,:]
	
	Error_Mat = np.empty([0,10])
	for i in range(3):
		if i==0:
			validation_set = d1
			Training_set = np.vstack((d2, d3))

		elif i==1:
			validation_set = d2
			Training_set = np.vstack((d1, d3))

		elif i==2:
			validation_set = d3
			Training_set = np.vstack((d1, d2))
		print("i:", i)
		score = Distance(validation_set, Training_set)
		print("score: ")
		print(score)
		m,n  = score.shape

		# storing the indexes of score_mat(row wise) in ascending order of the distances
		# idx[i][j] -> Tells the corresponding ith row in the Training_set with which the comparison done with 
		# jth data in the validation_set
		idx = np.empty([0,n], dtype=int)
		
		for j in range(0,m):
			# import pdb; pdb.set_trace()
			ind = np.argpartition(score[j],3)
			idx = np.vstack((idx,ind))
		
		print "idx:", '\n', idx
		actual_labels = validation_set[:,5]
		labels = np.empty([m,0])
		clone = np.zeros((m,1))
		# import pdb; pdb.set_trace()
		print "Training_set:"
		print Training_set 
		for k in range(1,20,2):
			arr = idx[:,0:k]
			m,_ = arr.shape
			
			print "k:", k
			for l in range(m):
				temp = []
				# import pdb; pdb.set_trace()
				for j in range(k):  #storing the corresponding labels
					temp.append(Training_set[arr[l][j],5])
				count = cl.Counter(temp)
				if count[0] > count[1]:
					clone[l][0] = 0
				else:
					clone[l][0] = 1
			
			labels = np.hstack((labels, clone))
		
		temp_error = FindError(labels, actual_labels)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																										
		Error_Mat = np.vstack((Error_Mat,temp_error))

	np.savetxt("Error_Mat.txt", Error_Mat)
	
	#computing std deviation of Error_mat for each k value
	std_dev = [np.std(Error_Mat[:,i]) for i in range(Error_Mat.shape[0])]

	Result = np.mean(Error_Mat,0)
	print ("Result:")
	print(Result)
	
	index = np.argmin(Result)
	k_suitable = 2*index + 1
	print("k:", k_suitable)

	return k_suitable

def main():

	Data = loadtxt("occupancy_data/datatraining.txt", delimiter="," , skiprows = 1, usecols=(2,3,4,5,6,7))
	print "For simple Knn type 0 or type 1 for modified version of Knn"
	inp = int(input())

	if inp==0:
		k1 = CrossValidation(Data)

	elif inp==1:
		k2 = ModCrossValidation(Data)

if __name__=="__main__":
	main()
