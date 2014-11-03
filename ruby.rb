#!/usr/bin/env ruby

# http://praxis.scholarslab.org/tutorials/ruby-cheatsheet/

# To invoke the REPL, use `irb`

# Strings
name = "Mark"
friend = 'Harry'
age = 40
sentence = name + ' is a guy who has age ' + age.to_s
sentence = "#{name} is a guy who has age #{age.to_s}"
'shout'.upcase
'shout'.downcase

var = 'this is a string'
var[0..5] # substring of 5 chars
a = "hello there"
a[1]                   #=> "e"
a[1,3]                 #=> "ell"
a[1..3]                #=> "ell"
a[-3,2]                #=> "er"
a[-4..-2]              #=> "her"
a[12..-1]              #=> nil
a[-2..-4]              #=> ""
a[/[aeiou](.)\1/]      #=> "ell"
a[/[aeiou](.)\1/, 0]   #=> "ell"
a[/[aeiou](.)\1/, 1]   #=> "l"
a[/[aeiou](.)\1/, 2]   #=> nil
a["lo"]                #=> "lo"
a["bye"]               #=> nil

out = out[-50..-1] # to the end

# Insert a variable with double quotes. Like PHP.
puts "Your name is #{name}"

# Shelling out
p = IO.popen(['fab', '-f', '/opt/titan/utilities/bindings.py', "converge:#{id}"]) #:err => [:child, :out]]
out = p.read
p.close
Chef::Log.warn("output = #{out}")
Chef::Log.warn("End of output")
Chef::Log.warn("status = #{$?.exitstatus}")

# Conditionals
my_var = 5
if my_var == 5 && other_var == 4
  puts "Success"
elsif my_var == 7
  puts "huh"
else
  puts "FAILURE"
end

log_entry['CHEF_EXCEPTION'] = run_status.exception if run_status.exception

# Hashes (or dictionaries)
store = {}
store['color'] = 'red'
stuff = {
  'mine' => 4,
  "other" => 55,
  :sym => 'a symbol was used as a key',
}

# 1.9 hash syntax
stuff = {
  mine: 'yours',
}

# Operators

# Ternary
puts (if 1 then 2 else 3 end) # => 2
puts 1 ? 2 : 3                # => 2

# @var is a member of the object
# :var is a symbol (special Ruby thing)

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
