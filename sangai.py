#!/usr/bin/env python

import getpass
import argparse
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

argparser = argparse.ArgumentParser(description="Generate password from passphrase")
argparser.add_argument('-l', dest="length", help="Generated password length", default=12)
argparser.add_argument('hint', nargs='*')
args = argparser.parse_args()

key = getpass.getpass() + args.hint[0];
len = int(args.length)
str = hashlib.sha512(str(key).encode("utf-8")).hexdigest()[:len];

print (str)
