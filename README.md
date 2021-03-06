<!-- language: lang-none -->
       __    __  ________  ________                              __             __
      |  \  |  \|        \|        \                            |  \           |  \
      | $$  | $$| $$$$$$$$| $$$$$$$$_______   _______   ______   \$$  ______  _| $$_
       \$$\/  $$| $$__    | $$__   /       \ /       \ /      \ |  \ /      \|   $$ \
        >$$  $$ | $$  \   | $$  \ |  $$$$$$$|  $$$$$$$|  $$$$$$\| $$|  $$$$$$\\$$$$$$
       /  $$$$\ | $$$$$   | $$$$$  \$$    \ | $$      | $$   \$$| $$| $$  | $$ | $$ __
      |  $$ \$$\| $$      | $$     _\$$$$$$\| $$_____ | $$      | $$| $$__/ $$ | $$|  \
      | $$  | $$| $$      | $$    |       $$ \$$     \| $$      | $$| $$    $$  \$$  $$
       \$$   \$$ \$$       \$$     \$$$$$$$   \$$$$$$$ \$$       \$$| $$$$$$$    \$$$$
                                                                      | $$
                                                                      | $$
                                                                       \$$
This repo contains a Python script to enumerate IP addresses in HTTP X-Forwarded-For field, and detect when a choosen status code is NOT returned. Can be used to find IP's to bypass 403 restrictions. This script is inspired by, and is an updated version of: https://github.com/omespino/enumXFF   

## DISCLAIMER
Use at your own risk. Usage might be illegal in certain circumstances.
Only for educational purposes!

### TODO:
- [ ] Reading IP range from file

# Setup

```
# Recomended to use virtual enviroment to keep your own enviroment clean
$ python3 -m venv venv && source venv/bin/activate

$ pip3 install -r requirements.txt
```

# Usage
```
$ python3 XFFscript.py -h
usage: XFFscript.py [-h] -t TARGET [-c STATUS_CODE] [-f FILE] [-r RANGE] [-w WORKERS] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Restricted Page (target)
  -c STATUS_CODE, --status_code STATUS_CODE
                        HTTP Status code to be ignored from response - default is 403
  -f FILE, --file FILE  Input file to read from
  -r RANGE, --range RANGE
                        IP range i.e. 0.0.0.0-255.255.255.255
  -w WORKERS, --workers WORKERS
                        Worker/thread count - default is 100
  -o OUTPUT, --output OUTPUT
                        If an IP address returns another status code, save IP address to file
```

# Example 
```
# Try common local IP addresses
$ python3 XFFscript.py -f common.txt -t http://www.restrictedpage.com/somedir/somefile
```

# License
Licensed using the MIT license. See [LICENSE.md](LICENSE.md)
