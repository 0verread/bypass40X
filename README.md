# bypass40X
Python script to bypass 40X 

python3 bypass40X.py -d example.com -p paths.txt

#### Installation

```
git clone https://github.com/0verread/bypass40X.git
cd bypass40X
python3 bypass40x.py -h
```

#### Usage

pythton3 bypass40x.py -d <target-domain> -p <pathlist> 
```bash

usage: bypass40x.py [-h] -d DOMAIN -p PATHLIST [-xh HEADER]

optional arguments:
  -h, --help            		show this help message and exit
  -d DOMAIN, --domain DOMAIN  	target domain
  -p PATH, --path PATHLIST  		File path dontains paths to bypass
  -xh HEADER, --header HEADER	Extra header
```

#### Features

1. Multiple path can be checked against one single domain
2. Verb tempering 
3. Support of extra header e.g. User-agent which is necessary to perform pentest on some targets. user-agent could be your name or unique identifier to standout in target machine log, so they know it's you and don't block your IP.