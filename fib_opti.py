def fib(n):
	if n<2:
		return n
	else:
		if not n-1 in fib_dic:
			fib_dic[n-1]=fib(n-1)
		if not n-2 in fib_dic:
			fib_dic[n-2]=fib(n-2)
		if n-1 in fib_dic and n-2 in fib_dic:
			return fib_dic[n-1]+fib_dic[n-2] 
		else:
			return fib(n-1)+fib(n-2)

fib_dic={}
result=fib(4)
print result
		
