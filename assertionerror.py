# To raise AssertionError if input is not between 10 and 20

try:
	a= int(input("Enter a number: "))
	assert a>=10 and a<=20, 'Invalid number'
	print("Accepted")

except AssertionError:
   print("Number is not between 10 and 20.")	
