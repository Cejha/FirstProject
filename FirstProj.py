import numpy as np

def myFunc(a,b):
	return np.array((a,b))

if __name__ == "__main__":
	print("Starting main...")
	a = 3
	b = 4
	arr = myFunc(a,b)
	print(arr)