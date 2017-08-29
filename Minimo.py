Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def minimo(arr):
	k=arr[0]
	for w in arr:
		if(w<k):
			k=w
			return k

		
>>> def ordenar(arr):
	arrsort=[]
	for k in range(len(arr)):
		w=minimo(arr)
		arr.remove(w)
		arrsort.append(w)
		return arrsort

	
>>> import random
>>> p = random.sample(range(2,102),100)
>>> cnt = 0
>>> print(p)
[59, 32, 49, 71, 16, 12, 72, 96, 58, 20, 88, 76, 101, 6, 47, 21, 87, 42, 85, 39, 24, 67, 46, 82, 89, 69, 27, 54, 70, 60, 31, 74, 28, 56, 64, 81, 90, 73, 29, 17, 5, 40, 77, 10, 79, 66, 68, 22, 11, 65, 52, 33, 7, 53, 51, 36, 9, 97, 55, 62, 50, 92, 63, 37, 95, 84, 35, 19, 86, 41, 26, 25, 4, 15, 94, 78, 99, 23, 98, 38, 34, 8, 14, 93, 83, 44, 13, 18, 43, 45, 80, 61, 2, 30, 100, 48, 91, 75, 57, 3]
>>> print(p[minimo(p)])
28
>>> print(min(p))
2
>>> print(ordenar(p))
[32]
>>> print(cnt)
0
>>> 
