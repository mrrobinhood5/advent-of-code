raw_data = []
File.open('input.txt', 'r') do |file|
  # Just opens file and dumps it into raw_data
  file.each_line do |line|
    raw_data << line
  end
end

def separate_lists(lines)
  # processes text in each data line into arrays or ints
  list_a = []
  list_b = []
  lines.each do |line|
    values = line.chomp.split('   ').map(&:to_i)
    list_a << values[0]
    list_b << values[1]
  end
  [list_a, list_b]
end

def get_distance(lines)
  # sorts and side by side finds distance in parallel
  list_a, list_b = lines.map(&:sort)
  dists = []
  list_a.zip(list_b).each do |a, b|
    dists << (a - b).abs
  end
  dists
end

def calculate_similarities(lines)
  list_a, list_b = lines
  sims = []
  list_a.each do |num|
    sims << num * list_b.count(num)
  end
  sims
end

puts calculate_similarities(separate_lists(raw_data)).sum
