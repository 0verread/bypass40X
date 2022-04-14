#!/usr/bin/python3

import sys
from os import popen

def make_request(domain, path):
	# make custom cURL requests
	uri = domain + path

def main():

	domain = sys.argv[1]
	paths  = sys.argv[2:len(sys.argv)]

	if not domain.startswith("http"):
		print("URL parameter doesn't start  with http or https")
		sys.exit(1)

	if len(paths) > 0 :
		# make the request with paths
		for path in paths:
			make_request(domain, path)


if __name__ == "__main__" :
	main()