# -1 indicates the blank in the given list of numbers
#############################################################################################


from collections import defaultdict
import numpy as np
# import queue
from Queue import PriorityQueue

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


# class node:
# 	def __init__(self, arr, cost=0)
# 	self.arr=arr
# 	self.cost=cost

# depth = 50
#############################################################################################
#			cost of array after moving a particular slide
#############################################################################################
def cost(ele):
	if np.any(ele in [1, 2, 3]):
		return 1
	elif np.any(ele in [3,4,5]):
		return 2
	else:
		return 3

#############################################################################################
# doing the comparison whether a particular state is equal to final state  
# if particular state == final state:
#		return true
# else:
#		pushing it into the stack
#############################################################################################
def check(l, pq, visit):
	bool_=0
	flag =0
	# import pdb; pdb.set_trace()
	if l != None:	
		for each in visit:
			if np.all(l[0] == each):
				bool_= 0	
				flag = 1
				break
		if flag == 0:
			if np.all(l[0]==final_state):
				bool_= 1

			else:
				if l != None:
					# import pdb;pdb.set_trace()
					pq.put(l[0], l[1])
	return (bool_, pq, visit)
#############################################################################################
##	returning the shifted matrix of blank to left, up, right and up
##
#############################################################################################
def left(arr):
	c=0
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column

	if j-1 < 0:
		return None
	else:
		c = cost(arr[i][j-1])
		k = arr[i][j]					#
		arr[i][j] = arr[i][j-1]			# Shifting -1 (blank) to the left by swapping 
		arr[i][j-1] = k                 #
		            
										
	return (arr,c)

def up(arr):
	c=0
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column

	if i-1 < 0:
		return None
	else:

		c = cost(arr[i-1][j])
		k = arr[i][j]					#
		arr[i][j] = arr[i-1][j]			# Shifting -1 (blank) to the up by swapping 
		arr[i-1][j] = k	
	# import pdb;pdb.set_trace()				#
	return (arr,c)


def right(arr):
	c=0
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column
	w,h = arr.shape
	if j+1 >= h:
		return None
	else:
		c = cost(arr[i][j+1])	
		k = arr[i][j]					#
		arr[i][j] = arr[i][j+1]			# Shifting -1 (blank) to the right by swapping 
		arr[i][j+1] = k				#
	return (arr,c)


def down(arr):
	c=0
	itemindex = np.where(arr==-1)		# returns tuple of arrs having (arr of rows, arr of columns)   
	i=itemindex[0][0]					# i-> row	
	j=itemindex[1][0]					#j->column
	w,h = arr.shape
	if i+1 >= w:
		return None
	else:
		c = cost(arr[i+1][j])
		k = arr[i][j]					#
		arr[i][j] = arr[i+1][j]			# Shifting -1 (blank) to the down by swapping 
		arr[i+1][j] = k					#
	return  (arr,c)

#############################################################################################
##		_dfs_() implemrnting dfs algorithm 
#############################################################################################
def _ufs_(array, pq, visited):
	count = 0
	while True:
		print "count: ",'\n', count
		count=count+1
		visited.append(array)

		temp = array + 0
		print "array:", array

		l1 = left(temp)
		# print "array:", array

		print "l1: ", '\n', l1
		# if l1 not in visited:
		(bool_,pq, visited) = check(l1 ,pq, visited)
		if bool_==1:
			return

		temp = array + 0
		l2 = up(temp)
		# print "array:",array

		print "l2: ",'\n' ,l2
		(bool_, pq, visited) = check(l2 , pq, visited)
		if bool_==1:
			return

		temp = array + 0
		l3 = right(temp)
		print "l3: ",'\n' ,l3
		(bool_, pq, visited) = check(l3 , pq, visited)	
		if bool_==1:
			return

		temp = array + 0
		l4 = down(temp)
		print "l4: ",'\n' ,l4
		(bool_, pq, visited) = check(l4 , pq, visited)
		# import pdb; pdb.set_trace()
		if bool_==1:
			return
		array = pq.get()
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

# pq = queue.PriorityQueue()
pq = MyPriorityQueue()
# initial_array = np.asarray(initial_state)
# _bfs_() returns final_state list i.e. ans_list
_ufs_(initial_array, pq, visited)

print "solved"

