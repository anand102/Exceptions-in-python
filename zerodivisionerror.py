a,b= [int(x) for x in input("Enter two numbers: ").split()]
try:
    c=a/b

    print("Result: ", c)
except ZeroDivisionError:
    print("Do not enter zero.")    


