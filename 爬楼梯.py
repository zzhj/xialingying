def pa(n):
	f=[0 for x in range(1000)]
	f[0]=0
	f[1]=1
	f[2]=2
	f[3]=4
	for i in range(4,n+1):
		f[i]=f[i-1]+f[i-2]+f[i-3]
	return f[n]

print (pa(100))
