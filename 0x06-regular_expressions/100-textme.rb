#!/usr/bin/env ruby

# Check if an argument is passed
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

# Read the log file
log_file = File.read(ARGV[0])

# Regular expression to extract sender, receiver, and flags
regex = /\[from:(?<sender>[^\]]+)\] \[to:(?<receiver>[^\]]+)\] \[flags:(?<flags>[^\]]+)\]/

# Match the regular expression in the log file
matches = log_file.scan(regex)

# Output the results
matches.each do |match|
  sender = match[0]
  receiver = match[1]
  flags = match[2]
  puts "#{sender},#{receiver},#{flags}"
end
