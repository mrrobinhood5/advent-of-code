# rubocop:disable Style/Documentation

require '../load_data.rb'
require 'minitest/autorun'
require 'pathname'

class Solution
  def initialize(type = :example, year = 2024, day = 1)
    @raw_data = if type == :example
                  load_example(Pathname.new('./test_input.txt'))
                else
                  load_data(day, year)
                end
  end

  def solution1
    puts @raw_data.inspect
    r = @raw_data.map do |line|
      x = line.chars.map(&:to_i).reject(&:zero?)
      "#{x.first}#{x.last}".to_i
    end
    puts r.inspect
    r.sum
  end

  def solution2
    0
  end
end

class ExamplesTest < Minitest::Test
  def setup
    @solution = Solution.new(:example, 2023, 1)
  end

  def test_solution_1_example
    assert_equal 142, @solution.solution1
  end

  def test_solution_2_example
    assert_equal 4, @solution.solution2
  end
end

solution = Solution.new(:real, 2023, 1)
puts solution.solution1.inspect
# puts solution.solution2.inspect
