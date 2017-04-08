import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import *


Data = loadtxt("Mod_Error_Mat.txt")
l=Data.tolist()
# err = open('error_matrix_mknn.txt','r') #comment out for normal knn and uncomment the below line...
# #err = open('error_matrix.txt','r')
# l = err.readline()
# l = l.split('][')
# l = [i.replace('[','') for i in l]
# l = [i.replace(']','') for i in l]
# l = [i.replace('\n','') for i in l]
# err.close()
# l = [i.split(',') for i in l]
# for i in range(len(l)):
#     l[i] = [float(p) for p in l[i]]
    #print l[i]
######################################################################
errors_std = []
for k in range(10):
    errors = [l[i][k] for i in range(3)]
    errors_std.append(np.std(errors))
    print "#", errors
    plt.scatter([2*k+1] * len(errors), errors)


errors_mean = map(lambda x,y,z:(x+y+z)/3.0,l[0],l[1],l[2])
print errors_mean
print errors_std

plt.errorbar(range(1,21,2), errors_mean, yerr = errors_std)
plt.title('Cross-validation on k')
plt.xlabel('k')
plt.ylabel('Cross-validation error')
plt.show()

#mean_error = map(lambda x,y,z:(x+y+z)/3.0,l[0],l[1],l[2])
#optimal_k = mean_error.index(min(mean_error))+1
#print 'Optimal k :',optimal_k
