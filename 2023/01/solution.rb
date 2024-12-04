# rubocop:disable Style/Documentation

require '../load_data.rb'
require 'minitest/autorun'
require 'pathname'

class Solution
  def initialize(type = :example, year = 2024, day = 1, filename)
    @raw_data = if type == :example
                  if filename.nil?
                    load_example(Pathname.new('./test_input.txt'))
                  else
                    load_example(Pathname.new(filename))
                  end
                else
                  load_data(day, year)
                end
  end

  def solution1
    r = @raw_data.map do |line|
      x = line.chars.map(&:to_i).reject(&:zero?)
      "#{x.first}#{x.last}".to_i
    end
    r.sum
  end

  def solution2
    # TODO: when implementing the parser use the equivalent of .startswith
    nums = {'one'=> 1, 'two'=> 2, 'three'=> 3, 'four'=> 4, 
            'five'=> 5, 'six'=> 6 , 'seven'=> 7, 'eight'=> 8, 
            'nine'=> 9, 'zero'=> 0}
    r = @raw_data.map do |line|
      nums.each do |word, digit|
        line.gsub!(word, digit.to_s)
      end
      line
    end
    puts r.inspect
    z = r.map do |line|
      x = line.chars.map(&:to_i).reject(&:zero?)
      "#{x.first}#{x.last}".to_i
    end
    puts z.inspect
    z.sum
  end
end

class ExamplesTest < Minitest::Test
  def setup
    @solution = Solution.new(:example, 2023, 1, './test_input.txt')
    @solution2 = Solution.new(:example, 2023, 1, './test_input2.txt')
  end

  def test_solution_1_example
    assert_equal 142, @solution.solution1
  end

  def test_solution_2_example
    assert_equal 281, @solution2.solution2
  end
end

solution = Solution.new(:real, 2023, 1)
puts solution.solution1.inspect
# puts solution.solution2.inspect
