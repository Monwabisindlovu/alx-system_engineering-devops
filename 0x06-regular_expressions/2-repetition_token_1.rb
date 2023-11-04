#!/usr/bin/env ruby

# Check if an argument is passed
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit 1
end

# Regular expression to match "hbn" with 'hbt' or 'hbtn' preceding it
regex = /hbt*n/

# Input text from the command line argument
input_text = ARGV[0]

# Find all matches in the input text
matches = input_text.scan(regex)

# Check if matches were found
if matches.empty?
  puts "No matches found."
else
  # Print each match found
  matches.each { |match| puts match }
end
