#!/usr/bin/python3

import sys
import argparse
from os import popen
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--domain", type=str, required=True, help="target domain")
parser.add_argument("-p", "--path", type=Path, required=True, help="File path dontains paths to bypass")
args = parser.parse_args()

def request_handler(domain=None, paths):
	# make custom cURL requests

	if domain is None:
		print("How the hell did you bypass required argument?? Lemme know.")
		sys.exit(1)

	uri = domain + path


def main():
	domain = args.domain
	pathlist  = args.path

	with open(pathlist) as file:
		paths = [path.rstrip() for path in file]
	
	print(paths)

	if not domain.startswith("http"):
		print("URL parameter doesn't start  with http or https")
		sys.exit(1)


if __name__ == "__main__" :
	main()