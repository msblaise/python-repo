def gcd(a, b):
	if a == 0 :
		return b
	
	return gcd(b%a, a)

# driver code 
a = 10
b = 15
print("gcd(", a , "," , b, ") = ", gcd(a, b))

a = 11
b = 2
print("gcd(", a , "," , b, ") = ", gcd(a, b))






