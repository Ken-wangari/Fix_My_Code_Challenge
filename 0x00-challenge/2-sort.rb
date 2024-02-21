result = ARGV.select { |arg| arg =~ /^-?[0-9]+$/ }.map(&:to_i).sort
puts result

