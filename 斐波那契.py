def fibo(n):
	f=[0 for x in range(100)]
	f[0]=0
	f[1]=1
	for i in range(2,n+1):
		f[i]=f[i-1]+f[i-2]
	return f[n]

print (fibo(8))
