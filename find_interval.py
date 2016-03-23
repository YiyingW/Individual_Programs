'''
Requested by Kaidi.
Functionality: 

Input: 1) read in a file containing lines with format
	   	  abc {[1:2]:10, [2:3]:20}
	   	  ...

	   	  note: there are at most 8 buckets.

	   	2) name of the object, e.g. abc, 
	   	   bucket number e.g.10

Output: interval for that bucket, 1:2


'''
def parser(filename):
	store = {}
	with open(filename, 'r') as f:
		rows = f.readlines()
		exlude = set(["{", "}", "[", "]"])
		for row in rows:
			items = row.split(' ')
			name = items[0]
			elements = ''.join(ch for ch in items[1] if ch not in exlude).strip('\n').split(',')
			value = []
			for element in elements:
				bucket = element.split(":")
				value.append((int(bucket[0]), int(bucket[1]), int(bucket[2])))
			store[name] = value
	return store

# given the name of object and the number of buck, return the interval
# note there are at most 8 bucks, if the number is greater than the stored amount, print error message
def read_buck(store, name, number):
	if name not in store.keys():
		print " there is no ", name, " in here."
	else:
		buck_number = len(store[name])
		if number > buck_number:
			print " there are not that many buckets."
		else:
			print "the interval is ", store[name][number-1][0], "to ", store[name][number-1][0]


			



store = parser('input1.txt')
read_buck(store, "CDE", 7)
