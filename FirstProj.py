import numpy as np

def myFunc(a,b):
    arrtemp = np.arange(a*b)
    arrreturn = np.reshape(arrtemp,(a,b))
    return arrreturn

if __name__ == "__main__":
	print("Starting main...")
	a = 3
	b = 4
	arr = myFunc(a,b)
	print(arr)
