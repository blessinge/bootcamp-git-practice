#Lodash for python
def unique(l):
	'''
	This function generate a list of unique values from l
	'''
	pass

def reverse(s):
	'''
	This function generates the reverse of s. s can be a string or a list. It returns the type given to it
	'''
	return s[::-1]

def intersection(a,b):
	'''
	This function returns the intersection of a and b - A list of common elements between a and b
	'''
	t = []
	for c in a:
		for d in b:
			if c == d:
				t[len(t)] = d
	return t


def generate(steps):
	pass

def parse_csv(csv_string):
	'''
	This function parses a CSV string as a list. The specification demands that the first row of data represents the column names
	'''
	pass

def frequency(needle, haystack):
	'''
	This function returns the number of times needle appears in haystack
	'''
	n = 0
	for f in haystack:
		if f == needle:
			n += 1
	return n

def sort(l):
	'''
	This function returns a sorted version of l
	'''
	return l.sort()