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
# Operators
#

# Ternary
result = a if test else b

# Lambda function - like anonymous.
log.pingdom = lambda msg: log.info(msg, SUBSYSTEM='pingdom')
log.pingdom('I have context')

##
# Debugging.
#
print 'You can print lots of things, remember to cast if using string concat operator: ' + str({'key': 'val'})

##
# Strings.
#
fruits = 'apple ' + ' orange'.upper()
fruit_len = len(fruits)
my_fav = 'My best fruits are %s and %s' % ('apple', 'jackfruit')
check_this = "This is another {0} of {1}".format('method', 'formatting')

# Convert unicode / byte
unicode(mystring)
str(mystring)

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

# Transform a dict
x = {k: [v] for k, v in dictionary.iteritems()}

##
# Lists (arrays). Can be changed (mutable).
#
games = ['squash', 'soccer', 'netball']
games.append('running')
games_string = ' and '.join(games)

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



