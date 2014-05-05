#!/usr/bin/env ruby

# http://praxis.scholarslab.org/tutorials/ruby-cheatsheet/

# Strings
name = "Mark"
friend = 'Dick'
sentence = name + " is a guy"
'shout'.upcase

# Insert a variable with double quotes. Like PHP.
puts "Your name is #{name}"

# Conditionals
my_var = 5
if my_var == 5 
  puts "Success" 
else 
  puts "FAILURE" 
end

# Hashes (or dictionaries)
store = {}
store['color'] = 'red'

store.has_key?('color') # true
store.length # 1

# Arrays
my_array = [1, 'hello', 220]

# Iteration
[1, 2, 3].each do | value |
  puts value
end

# Functions
def assert_equal(expected, actual) 
  if expected != actual 
    puts "FAILURE!" 
  end 
end
