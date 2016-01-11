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

key = getpass.getpass()
len = int(args.length)
str = hashlib.sha512(key + args.hint[0]).hexdigest()[:len];

print str
