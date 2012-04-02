def inc(n):
	return n+1
def dec(n):
	return n-1

def sum(a,b):
# return(inc(a)+dec(b))
	
	if b==0:
		return a
	else:
	        return sum(inc(a),dec(b))	

c=sum(5,10)
print c

