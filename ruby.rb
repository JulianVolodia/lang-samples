#!/usr/bin/env ruby

# http://praxis.scholarslab.org/tutorials/ruby-cheatsheet/

# Strings
name = "Mark"
friend = 'Harry'
age = 40
sentence = name + " is a guy who has age " + age.to_s
'shout'.upcase
'shout'.downcase

# Insert a variable with double quotes. Like PHP.
puts "Your name is #{name}"

# Conditionals
my_var = 5
if my_var == 5
  puts "Success"
elsif my_var == 7
  puts "huh"
else
  puts "FAILURE"
end

# Hashes (or dictionaries)
store = {}
store['color'] = 'red'
stuff = {'mine' => 4}

store.has_key?('color') # true
store.length # 1

store.each do |key, val|
  puts key
  puts val
end

# Arrays
my_array = [1, 'hello', 220]
my_array.delete(1)
my_array.delete('hello')

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
