#!/usr/bin/env ruby

# Define a regular expression to extract the desired information
regex = /\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/

# Check if the script was provided with an argument
if ARGV.length == 1
  input = ARGV[0]

  # Use the regular expression to extract the desired information
  match_data = input.match(regex)

  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]

    # Output the extracted information
    puts "#{sender},#{receiver},#{flags}"
  else
    puts "No match found in the input."
  end
else
  puts "Usage: #{$0} <log_entry>"
end
