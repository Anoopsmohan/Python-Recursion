def fact(f,n):
	if n==1:
		return f
	else:
		return fact(f*n,n-1)



a=fact(1,3)
print a
