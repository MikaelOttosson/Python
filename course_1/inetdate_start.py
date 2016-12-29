# Get data from urllib

import urllib2

def main():

	webUrl = urllib2.urlopen("http://www.sunet.se")

	print "Result code: " + str(webUrl.getcode())

	data = webUrl.read()
	print data


if __name__ == '__main__':
	main()