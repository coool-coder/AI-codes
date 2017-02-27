# -1 indicates the blank in the given list of numbers
#############################################################################################


from collections import defaultdict
import numpy as np
from queue import *
import sys
import time 
import resource
from pythonds.pythonds.basic.stack import Stack


class node:
	def __init__(self, data, order=""):
		self.data = data
		self.order = order


#############################################################################################
# doing the comparison whether a particular state is equal to final state  
# if particular state == final state:
#		return true
# else:
#		pushing it into the queue 
#############################################################################################
def check(l, q):
	flag =0
	# import pdb; pdb.set_trace()
	if l.data!=None:
		for each in visited:
			if np.all(l.data == each):
				flag = 1
				break
		if flag == 0:
		 	q.put(l)
	return q
#############################################################################################
##	returning the shifted matrix of blank to left, up, right and up
##
#############################################################################################
def left(arr):
	itemindex = np.where(arr==0)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column

	if j-1 < 0:
		return None
	else:
		k = arr[i][j]					#
		arr[i][j] = arr[i][j-1]			# Shifting -1 (blank) to the left by swapping 
		arr[i][j-1] = k						#
	return arr

def up(arr):
	itemindex = np.where(arr==0)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column

	if i-1 < 0:
		return None
	else:
		k = arr[i][j]					#
		arr[i][j] = arr[i-1][j]			# Shifting -1 (blank) to the up by swapping 
		arr[i-1][j] = k					#
	return arr


def right(arr):
	itemindex = np.where(arr==0)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column
	w,h = arr.shape
	if j+1 >= h:
		return None
	else:
		k = arr[i][j]					#
		arr[i][j] = arr[i][j+1]			# Shifting -1 (blank) to the right by swapping 
		arr[i][j+1] = k					#
	return arr


def down(arr):
	itemindex = np.where(arr==0)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column
	w,h = arr.shape
	if i+1 >= w:
		return None
	else:
		k = arr[i][j]					#
		arr[i][j] = arr[i+1][j]			# Shifting -1 (blank) to the down by swapping 
		arr[i+1][j] = k					#
	return arr

#############################################################################################
##		_bfs_() implemrnting bfs algorithm 
#############################################################################################
def _bfs_(array):
	count=0
	# queue is for operatiion purpose--> to choose the next state (for bfs implementation)
	q = Queue(maxsize=0)
	q.put(array)
	string = ""
	maxsize=0
	while True:
		if maxsize < q.qsize():
			maxsize = q.qsize()
		# removing one element from the frontier set
		array = q.get()
		# Matching the state with the final state
		if np.all(array.data==final_state):
			return (array, q.qsize(), maxsize)

		visited.append(array.data)

		temp = array.data + np.zeros((3,3))
		l1 = node(temp, "")
		l1.data = up(temp)
		l1.order= array.order + "U"		
		q = check(l1 , q)
		
		if array.data!=None:
			temp = array.data + np.zeros((3,3))
		l2 = node(temp, "")
		l2.data = down(temp)
		l2.order= array.order+"D"
		q = check(l2 , q)
		

		temp = array.data + np.zeros((3,3))
		l3 = node(temp, "")
		l3.data = left(temp)
		l3.order= array.order+"L"
		q = check(l3 , q)
			
		temp = array.data + np.zeros((3,3))
		l4 = node(temp, "")
		l4.data = right(temp)
		l4.order= array.order+"R" 
		q = check(l4 , q)	
		
############################################################################################
##											main
##
#############################################################################################

def main(argv):
	method = argv[0]
	# input_mat 	= argv[1:]
	input_str = argv[1]
	input_list = input_str.split(',')


	initial_state = [int(x) for x in input_list]

	global final_state
	final_state = np.array([[0,1,2],[3,4,5],[6,7,8]])

	# visited array for keeping track of the state that are visited once --> to avoid repeatance
	global visited
	visited = list()

	initial_array = np.asarray(initial_state)
	initial_array.resize((3, 3))
	
	mat = node(initial_array, "")
	start_time= time.time()
	start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	
	if method=="bfs":
		(mat, length, maxSize) = _bfs_(mat)
	elif method=="dfs":
		(mat,length, maxSize) = _dfs_(mat)
	elif method=="ast":
		(mat,length, maxSize) = _ast_(mat)
	elif method=="ida":
		(mat, length, maxSize) = _ida_(mat)

	print ("time: ", time.time()-start_time)
	print (mat.data, mat.order)
	print ("no. of nodes expanded: ", length)
	print ("len(visited): ",  len(visited))
	print ("maxSize: ",  maxSize)
	print("Search Depth: ", len(mat.order))
	delta_mem = (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) - start_mem
	print("delta_mem: ", delta_mem/1024.0)
	
if __name__== "__main__":
	main(sys.argv[1:])