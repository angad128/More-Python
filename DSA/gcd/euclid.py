def euclid(m,n):
	if(m<n):
		(m,n) = (n,m)
	print()

 	if ((m%n)== 0):
 		return(n)
 	else:
 		diff = m-n
 		return(gcd(max(n,diff),min(n,diff)))

print(12,144)