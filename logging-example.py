import logging

logging.basicConfig(filename= 'test.txt', level= logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of script')

def factorial(n):
	
	logging.debug('Start of factorial(%s)' % (n))
	total = 1
	for x in range (1, n + 1):
		
		total *= x
		logging.debug('x is ' + str(x) + ', total is ' + str(total))
	
	logging.debug('End of factorial(%s)' % (n))
	return total

variable = 10
print('The factorial of', str(variable), 'is', factorial(variable), '.')
logging.debug('End of script')
