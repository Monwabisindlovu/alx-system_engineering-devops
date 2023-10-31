#!/usr/bin/env ruby

# Check if an argument is passed
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Regular expression to match capital letters
regex = /[A-Z]/

# Input text from the command line argument
input_text = ARGV[0]

# Match the regular expression in the input text and join the results
match = input_text.scan(regex).join

# Print the matched result
puts match
