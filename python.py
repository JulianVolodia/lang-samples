#!/usr/bin/env python

##
# Modules.
#
import os.path
from os.path import getmtime

try:
  import huhhiya
except ImportError:
  mod_not_found = True

if os.path.exists('/home'):
  found_home = True

mtime = getmtime('/home')

##
# Time conversion ISO 8601
#
import dateutil.parser
from datetime import datetime
datestring = "2014-10-07T07:11:52.158Z"
yourdate = dateutil.parser.parse(datestring)

##
# Regular expressions
#
import re
re.search('needle', 'haystack-haystack-haystack-haystack-needle-haystack')

match = re.search('^(\+|\-)Subproject commit [A-Fa-f0-9]{40}$', diff.patch, flags=re.MULTILINE)
  if match:
      print match.group(0)

##
# Time and Sleep
#

import time
time.sleep(seconds)

##
# Exceptions
#
try:
    self.sync_code()
  except Exception as e:
    sys.stderr.write(json.dumps({
      'type': e.__class__.__name__,
      'value': str(e)
    }))

raise Exception("I know python!")

##
# Subprocess, making shell calls / commands
# @see: http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
#
subprocess.check_call("cd /etc/systemd/system && systemctl restart")

##
# Operators
#

# There is no ++ or -- operator in Python. Use += or -=.

# Ternary
result = a if test else b

# Lambda function - like anonymous.
log.pingdom = lambda msg: log.info(msg, SUBSYSTEM='pingdom')
log.pingdom('I have context')

# No && operator in Python.
if a == 4 and b == 5:
  print 'match'

##
# Loops
#
while True:
  print 'loop-de-loop'

##
# Debugging.
#
print 'You can print lots of things, remember to cast if using string concat operator: ' + str({'key': 'val'})

# Pretty print stuff
from pprint import pprint
pprint(data)
pprint(e, stream=sys.stderr)

from pprint import pprint
pprint (vars(your_object))

dir(your_object)

# For debugging. Use it to print out OrderedDicts
def jdump(obj):
    print json.dumps(obj,indent=4)

# Check if a list, dict, OrderedDict is empty. Don't use len(od)
if od:
if not od:

# Works nicely for ygg objects.
vars(obj)

##
# Strings. Single and double quotes are basically interchangeable and are convenient
# when you don't want to escape, e.g. 'I want to "quote" stuff'. Other than that no
# difference.
#
fruits = 'apple ' + ' orange'.upper()
fruit_len = len(fruits)
my_fav = 'My best fruits are %s and %s' % ('apple', 'jackfruit')
check_this = "This is another {0} of {1} used in Python 3".format('method', 'formatting')

# If you need to include a brace character in the literal text, it can be escaped by doubling: {{ and }}.
# Don't use \{ \} that doesn't work.
check_this = "This is {{another}} {0} of {1} used in Python 3".format('method', 'formatting')

# Split / explode strings
pieces = "this is a string".split(' ')

# Convert unicode / byte
unicode(mystring)
str(mystring)

# Check what a string is - unicode or byte.
s = u"Test"
isinstance(s, basestring)
isinstance(s, unicode)
isinstance(s, str)

# Check if a string contains a substring
if "blah" not in somestring: continue

# Trim / strip chars from string
text = "hello"
text.rstrip('o')
text.lstrip('h')

path = "/users/"
path.strip("\/")

##
# Dictionaries.
#
hosts = dict(one=1, two=2)
hosts = dict({'one': 1, 'two': 2})
hosts = dict(zip(('one', 'two'), (1, 2)))
hosts = dict([['two', 2], ['one', 1]])
hosts = {'one': 1, 'two': 2}

# Simple operations on dictionaries.
hosts['three'] = 3
hosts['four'] = None
num_hosts = len(hosts)

# When getting a value, prefer .get() as it will check for existence of the key
hosts.get('three')
hosts.get('doesnotexist') # returns None

# Does a key exist in a dict?
if key in dict:
  print 'Yes'
return self.count() and any(val['id'] == key for val in dictionary.values())

# Remove a key from a dict
if ('one' in hosts):
  del hosts['one']

# Iterating over dictionaries.
for host in hosts:
  if (hosts[host] is not None):
    hosts[host] = hosts[host] + 1

for k, v in hosts.iteritems():
  msg = 'The key is ' + str(k) + ' and the value is ' + str(v)

# Comprehension of a dict, transform a dict
mydict = {}
mydict['one'] = {'type':'red','env':'dev'}
mydict['two'] = {'type':'red','env':'live'}
# mydict = {'two': {'type': 'red', 'env': 'live'}, 'one': {'type': 'red', 'env': 'dev'}}
x = {k: [v] for k, v in dictionary.iteritems() if v['env'] == 'dev'}
# x = {'one': [{'type': 'red', 'env': 'dev'}]}

##
# Lists (arrays). Can be changed (mutable).
#
games = ['squash', 'soccer', 'netball']
games.append('running')
games_string = ' and '.join(games)
if type([1,2]) is list:
  print "It's a list!"

# Concatenating lists is easy
othergames = ['rugby']
games = games + othergames

sorted_games = sorted(games)

##
# Tuples (immutable). Position has meaning.
#
pointcloud = (23, 100, 0)

##
# Sets.
#
favorite_fruit = set(['bananas', 'oranges', 'pears', 'guavas'])
fruit_bowl = set(['bananas'])
to_buy = favorite_fruit - fruit_bowl

##
# Functions.
#
def myfunc(arg1, arg2):
  """
  It's customary to comment in blocks using the triple-quoted string.
  """
  val1 = 'username/' + arg1
  val2 = 'password/' + arg2
  return val1, val2
user,password = myfunc('mark', 'secret')

# Passing list as function parameters
args = ['steve', '12345']
user,password = myfunc(*args)

##
# File IO
#
data = open('file.ext')

##
# Types.
#
msg = 3
type(msg)

##
# JSON
#
import json
json_data = open('ucb_sites.json')
data = json.load(json_data)

##
# HTTP GET request
#
import urllib2
urllib2.urlopen("http://example.com/foo/bar").read()

##
# Return an unused socket number.
#
# Binds to 0, which means the kernel will allocate a free socket.
#
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
addr = s.getsockname()
print addr[1]
s.close()

##
# Casting
#
a = '3'
b = int(a) + 2
