

def main():
	x, y = 100, 100

	if(x < y):
		st = "x is less then y"
	elif (x == y):
		st = "x is same as y"
	else:
		st = "x is greater then y"
	print st

	st = "x is less the y" if (x < y) else "x is greater then or equal to y"
	print st

if __name__ == '__main__':
	main()