def power(x,y):
	if y==0:
		return 1
	elif x==0:
		return 0
	elif y%2==0:
		return power(x,y/2)*power(x,y/2)
	else:
		y=(y-1)/2
		return x*power(x,y)*power(x,y)
	
result=power(2,3)
print result
