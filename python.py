#!/usr/bin/env python

##
# Modules.
#
import os.path
from os.path import getmtime

if os.path.exists('/home'):
  found_home = True

mtime = getmtime('/home')

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

if ('one' in hosts):
  del hosts['one']

# Iterating over dictionaries.
for host in hosts:
  if (hosts[host] is not None):
    hosts[host] = hosts[host] + 1

for k, v in hosts.iteritems():
  msg = 'The key is ' + str(k) + ' and the value is ' + str(v)

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



