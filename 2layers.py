import numpy as np
# input dataset
x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
# output dataset            
y = np.array([[0,0,1,1]]).T

# start
np.random.seed(1)
w0 = 2 * np.random.random((3,4)) - 1
w1 = 2 * np.random.random((4,1)) - 1
# l0 > w0 > l1 > w1 > l2 (y)
for i in range(60000):
	l0 = x
	l1 = 1/(1+np.exp(-(np.dot(l0,w0))))
	l2 = 1/(1+np.exp(-(np.dot(l1,w1))))
	delta1 = (y - l2)*(l2*(1-l2)) #(4,1)
	delta0 = delta1.dot(w1.T)*(l1*(1-l1))
	w1 += np.dot(l1.T, delta1)
	w0 += np.dot(l0.T, delta0)
	
print(l2)
