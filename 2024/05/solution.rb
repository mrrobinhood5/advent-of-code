require '../load_data.rb'
require 'minitest/autorun'
require 'pathname'

$year = 2024
$day = 5
$test_file = './test_input.txt'

def load_example(filename)
  rules, ordering = File.open(filename).read.split("\n\n").map(&:split)
  # [rules.split("|"), ordering.split(",")]
end

def load_data(day, year)
  url = URI.parse("https://adventofcode.com/#{year}/day/#{day}/input")
  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = (url.scheme == 'https')
  cookie = File.open('../.session').readline.chomp!
  request = Net::HTTP::Get.new(url.request_uri)
  request['Cookie'] = "session=#{cookie}"
  response = http.request(request)
  rules, ordering = response.body.split("\n\n").map(&:split)
  # [rules.split("|"), ordering.split(",")]
end

class Solution
  def initialize(type = :example, year = $year, day = $day, filename = $test_file)
    @raw_data = if type == :example
                  load_example(Pathname.new(filename))
                else
                  load_data(day, year)
                end
  end

  def middle_of_array(line)
    line[line.length/2]
  end

  def solution1
    @rules, @ordering = @raw_data
    passed = @ordering.select do |order|
      @rules.map do |rule|
        a, b = rule.split("|")
        if order.match(/(?=.*#{a})(?=.*#{b})/)
          !order.match(/(?<=#{a}).*(?=#{b})/).nil?
        else
          next
        end
      end.compact.all?
    end
    passed.sum do |line|
      middle_of_array(line.split(",").map(&:to_i))
    end
  end

  def solution2
    @rules, @ordering = @raw_data
    failed = @ordering.select do |order|
      @rules.map do |rule|
        a, b = rule.split("|")
        if order.match(/(?=.*#{a})(?=.*#{b})/)
          order.match(/(?<=#{a}).*(?=#{b})/).nil?
        else
          next
        end
      end.compact.any?
    end
    puts failed.inspect()
     @ordering = failed.map do |line|
      line.split(",").permutation.to_a
    end.flatten(1)
    solution1
    # fails i think because there are multiple permutations that pass all tests
  end

end

class ExamplesTest < Minitest::Test
  def setup
    @solution = Solution.new(:example, $year, $day)
    @solution2 = Solution.new(:example, $year, $day)
  end

  def test_solution_1_example
    assert_equal 143, @solution.solution1
  end

  def test_solution_2_example
    assert_equal 123, @solution2.solution2
  end
end

# solution = Solution.new(:real, $year, $day)
# puts solution.solution1.inspect
# puts solution.solution2.inspect
