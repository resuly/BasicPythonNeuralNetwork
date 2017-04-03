import numpy as np
# input dataset
x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
# output dataset            
y = np.array([[0,0,1,1]]).T

# start
np.random.seed(1)
w0 = 2 * np.random.random((3,1)) - 1
for i in range(1000):
	l0 = x
	l1 = 1/(1+np.exp(-(np.dot(l0,w0))))
	delta = (y - l1)*(l1*(1-l1))
	w0 += np.dot(l0.T, delta)

print(l1)