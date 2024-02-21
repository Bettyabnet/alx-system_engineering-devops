regex = /School/

input = ARGV[0]

if input.match?(regex)
  puts 'School'
else
  puts ''
end
