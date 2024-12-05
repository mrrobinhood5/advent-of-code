# rubocop:disable Style/Documentation

require '../load_data.rb'
require 'minitest/autorun'
require 'pathname'

class Solution
  def initialize(type = :example, year = 2024, day = 1, filename = './test_input.txt')
    @raw_data = if type == :example
                  load_example(Pathname.new(filename))
                else
                  load_data(day, year)
                end
  end

  def solution1
    @raw_data.flat_map do |line|
      line.scan(/mul\((\d+),(\d+)\)/).map do |a, b|
        a.to_i * b.to_i
      end
    end.sum
  end

  def solution2
    @raw_data = @raw_data.join("\n")
    clearing = /(?=don't\(\))(.*?)(?=do\(\))/m
    @raw_data = @raw_data.gsub(clearing, "")
    @raw_data.scan(/mul\((\d+),(\d+)\)/).map {|a, b| a.to_i * b.to_i}.sum



    # data = @raw_data.join
    # matching = /mul\((\d+),(\d+)\)/
    # filtered_data = data.gsub(clearing, "")
    # filtered_data.scan(matching).map do |a, b|
    #   a.to_i * b.to_i
    # end.sum
 
  end
end

class ExamplesTest < Minitest::Test
  def setup
    @solution = Solution.new(:example, 2024, 3)
    @solution2 = Solution.new(:example, 2024, 3, './test_input2.txt')
  end

  def test_solution_1_example
    assert_equal 161, @solution.solution1
  end

  def test_solution_2_example
    assert_equal 48, @solution2.solution2
  end
end

solution = Solution.new(:real, 2024, 3)
puts solution.solution1.inspect
puts solution.solution2.inspect
