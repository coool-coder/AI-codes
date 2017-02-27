# 0 indicates the blank in the given list of numbers
#############################################################################################

from collections import defaultdict
import numpy as np
from pythonds.pythonds.basic.stack import Stack

depth = 50
#############################################################################################
# doing the comparison whether a particular state is equal to final state  
# if particular state == final state:
#		return true
# else:
#		pushing it into the stack
#############################################################################################
def check(l, s, visit):
	bool_=0
	flag =0
	# import pdb; pdb.set_trace()
	for each in visit:
		if np.all(l == each) == True:
			bool_= 0	
			flag = 1
			break
	if flag == 0:
		if np.all(l==final_state):
			bool_= 1

		else:
			if l != None:
				s.push(l)
	return (bool_, s, visit)
#############################################################################################
##	returning the shifted matrix of blank to left, up, right and up
##
#############################################################################################
def left(arr):
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
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
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
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
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
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
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
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
##		_dfs_() implemrnting dfs algorithm 
#############################################################################################
def _dfs_(array, s, visited):
	count = 0
	while True:
		print("count: ", count, sep='\n')
		count=count+1
		visited.append(array)
		temp = array + 0
		print ("array:", array, sep='\n')

		l1 = left(temp)
		# print ("array:", array, sep='\n')

		print ("l1: ", l1, sep='\n')
		# if l1 not in visited:
		# import pdb;pdb.set_trace()
		(bool_, s, visited) = check(l1 , s, visited)
		if bool_==1:
			return

		temp = array + 0
		l2 = up(temp)
		# print ("array:",array, sep='\n')

		print ("l2: ", l2, sep='\n')
		(bool_, s, visited) = check(l2 , s, visited)
		if bool_==1:
			return

		temp = array + 0
		l3 = right(temp)
		print ("l3: ", l3, sep='\n')
		(bool_, s, visited) = check(l3 , s, visited)	
		if bool_==1:
			return

		temp = array + 0
		l4 = down(temp)
		print ("l4: ", l4,sep='\n')
		(bool_, s, visited) = check(l4 , s, visited)
		# import pdb; pdb.set_trace()
		if bool_==1:
			return
		array = s.pop()
	# import pdb; pdb.set_trace()
	# _bfs_(q.get(), q, visited)

#############################################################################################
##											main
##
#############################################################################################
# initial_state = input("enter 1 to 8 numbers in a 3x3 list as your initial state and put -1 in list where u want to provide blank: ")   # taking input a list
# final_state = input("enter 3x3 list as your goal state: ")   # taking input a list
initial_state = np.array([[1,2,3],[4,-1,6],[7,5,8]])
global final_state
final_state = np.array([[1,2,3],[4,5,6],[7,8,-1]])

# visited array for keeping track of the state that are visited once --> to avoid repeatance
visited = list()

# queue is for operatiion purpose--> to choose the next state (for bfs implementation)
s = Stack()
initial_array = np.asarray(initial_state)
# _bfs_() returns final_state list i.e. ans_list
_dfs_(initial_array, s, visited)

print ("solved")

