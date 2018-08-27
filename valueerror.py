# value error

try:
	a,b= [int(x) for x in input("Enter two numbers: ").split()]
	c=a/b

	print("Result is : ",c)

except ValueError:
    print("Enter Integer number only.")	