# creating a log file

import logging
logging.basicConfig(filename="mylog.txt", level=logging.ERROR)

try:
	a,b=[int(i) for i in input('Enter two numbers: ').split()]
	c=a/b
	print('Result is:  ', c)
except Exception as e:
	logging.exception(e)
	