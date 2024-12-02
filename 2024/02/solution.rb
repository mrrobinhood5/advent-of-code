# rubocop:disable Style/Documentation

require '../load_data.rb'
require 'minitest/autorun'
require 'pathname'

class Solution
  def initialize(type = :example, year = 2024, day = 1)
    if type == :example
      @raw_data = load_example(Pathname.new('./test_input.txt'))
    else
      @raw_data = load_data(day, year)
    end
  end

  def solution1
  end

  def solution2
  end
end

class ExamplesTest < Minitest::Test
  def setup
    @solution = Solution.new :example, 2024, 2
  end

  def test_solution_1_example
    assert_equal 11, @solution.solution1
  end

  def test_solution_2_example
    assert_equal 31, @solution.solution2
  end
end
