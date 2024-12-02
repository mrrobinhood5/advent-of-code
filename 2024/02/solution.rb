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

  def find_levels(line)
    line.each_cons(2).map { |a, b| a - b }
  end

  def safe?(level_line)
    level_line.none? { |x| x.abs > 3 } && same_direction?(level_line)
  end

  def same_direction?(level_line)
    level_line.all?(&:positive?) || level_line.all?(&:negative?)
  end

  def solution1
    data = @raw_data.map { |line| line.split(' ').map(&:to_i) }
    levels = data.map { |line| find_levels(line) }
    safe = levels.map { |line| safe?(line) }
    safe.count(true)
  end

  def solution2
    data = @raw_data.map { |line| line.split(' ').map(&:to_i) }
    data.count do |line|
      levels = find_levels(line)
      next true if safe?(levels)

      line.each_index.any? do |x|
        temp_line = line.dup
        temp_line.delete_at(x)
        safe?(find_levels(temp_line))
      end
    end
  end
end

class ExamplesTest < Minitest::Test
  def setup
    @solution = Solution.new(:example, 2024, 2)
  end

  def test_solution_1_example
    assert_equal 2, @solution.solution1
  end

  def test_solution_2_example
    assert_equal 4, @solution.solution2
  end
end

solution = Solution.new(:real, 2024, 2)
puts solution.solution1.inspect
puts solution.solution2.inspect
