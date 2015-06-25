# -*- coding: utf-8 -*-

"""

Reversed iteration only works if the object in question has a size
 that can be determined or if the object implements 
 a __reversed__() special method. If neither of these can be 
 satisfied, you’ll have to convert the object into a list first.

Be aware that turning an iterable into a list could consume a 
lot of memory if it’s large.

Defining a reversed iterator makes the code much more efficient, 
as it’s no longer necessary to pull the data into a list and 
iterate in reverse on the list.

"""

class Countdown:
	def __init__(self, start):
		self.start = start

	#Forward iterator
	def __iter__(self):
		n = self.start
		while n > 0:
		    yield n
		    n -= 1

	#Reverse iterator

	def __reversed__(self):
		    n = 1
		    while n <= self.start:
		    	yield n
		    	n += 1


if __name__ == '__main__':
	c = Countdown(5)
	for n in reversed(c):
		print(n)

