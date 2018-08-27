# Creating a user defined exception

class MyException(Exception):
	def __init__(self, str):
		self.str=str

def check(dict):
	for k,v in dict.items():
		print(k,v)
		if v<=2000:
			raise MyException("Account Balance is low!")
# raise is used to raise our user defined exceptions.

mydict= {'Gopal': 2800.00, 'Amit': 5600.00, 'Yash': 1990.00, 'Preeti':2500.00}	

try:
    check(mydict)
except MyException as e:
    print(e)    		


