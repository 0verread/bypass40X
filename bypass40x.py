#!/usr/bin/python3

import sys
import argparse
from os import popen
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--domain", type=str, required=True, help="target domain")
parser.add_argument("-p", "--path", type=Path, required=True, help="File path dontains paths to bypass")
parser.add_argument("-ua", "--user-agent", type=str, required=False, help="user-agent header")
args = parser.parse_args()

# support for user-aget
# support for custom header
# 
def make_curl_request(url):
	print(url)
	code = popen("curl -k -s -I %s | grep HTTP"%(url)).read()
	return code

# TODO: make different urls and pass to make_curl_request 
def do_bypass(url):
	code  = make_curl_request(url)
	status_code = code.split(" ")[1]
	print(f"{status_code} : {url}")

def request_handler(domain, paths):
	if domain is None:
		print(f"How the hell did you bypass required argument?? Lemme know.")
		sys.exit(1)

	for path in paths:
		whole_path = domain + path
		do_bypass(whole_path)

def main():
	domain = args.domain
	pathlist  = args.path

	with open(pathlist) as file:
		paths = [path.rstrip() for path in file]
	

	if not domain.startswith("http"):
		print(f"URL parameter doesn't start  with http or https")
		sys.exit(1)
	if len(paths) == 0:
		print(f"Path file is empty.")
		sys.exit(1)

	request_handler(domain, paths)

if __name__ == "__main__" :
	main()