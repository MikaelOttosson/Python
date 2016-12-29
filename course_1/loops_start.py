#
#
#

def main():
	x = 0

	while (x < 5):
		print x
		x = x + 1

	for x in range(5, 10):
		print x


	# Loop over a "Collection"
	days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	for d in days:
		print d


	# Use break and continue statements
	for x in range(5,10):
		if (x == 7): break
		if (x % 2 == 0): continue
		print x


	# use enumerate() funtion to get index
	days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	for i in enumerate(days):
		print i, d
		

if __name__ == '__main__':
	main()

