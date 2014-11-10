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
# Operators
#

# There is no ++ or -- operator in Python. Use += or -=.

# Ternary
result = a if test else b

# Lambda function - like anonymous.
log.pingdom = lambda msg: log.info(msg, SUBSYSTEM='pingdom')
log.pingdom('I have context')

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

##
# Strings.
#
fruits = 'apple ' + ' orange'.upper()
fruit_len = len(fruits)
my_fav = 'My best fruits are %s and %s' % ('apple', 'jackfruit')
check_this = "This is another {0} of {1} used in Python 3".format('method', 'formatting')

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

##
# Dictionaries.
#
# The many ways to create a dictionary.
hosts = dict(one=1, two=2)
hosts = dict({'one': 1, 'two': 2})
hosts = dict(zip(('one', 'two'), (1, 2)))
hosts = dict([['two', 2], ['one', 1]])
hosts = {'one': 1, 'two': 2}

# Simple operations on dictionaries.
hosts['three'] = 3
hosts['four'] = None
num_hosts = len(hosts)

# Remove a key from a dict
if ('one' in hosts):
  del hosts['one']

# Iterating over dictionaries.
for host in hosts:
  if (hosts[host] is not None):
    hosts[host] = hosts[host] + 1

for k, v in hosts.iteritems():
  msg = 'The key is ' + str(k) + ' and the value is ' + str(v)

# Does a key exist in a dict?
if key in dict:
  print "Yes"

return self.count() and any(val['id'] == key for val in dictionary.values())

# Transform a dict
x = {k: [v] for k, v in dictionary.iteritems()}

##
# Lists (arrays). Can be changed (mutable).
#
games = ['squash', 'soccer', 'netball']
games.append('running')
games_string = ' and '.join(games)
if type([1,2]) is list:
  print "It's a list!"

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
