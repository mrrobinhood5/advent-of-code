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

  def two_side_count(line)
    line.scan(@term).count + line.reverse.scan(@term).count
  end

  def transpose_lines(data_set)
    data_set.map(&:chars).transpose.map(&:join)
  end

  def get_diagonals(data) 
    rows = data.map(&:chars) 
    diagonals = [] 
    (0...rows.size).each do |k| 
      diagonals << (0..k).map { |i| rows[i][k - i] }.join 
      end 
    (1...rows[0].size).each do |k| 
      diagonals << (0...rows.size - k).map { |i| rows[k + i][rows.size - 1 - i] }.join
      end 
    diagonals 
  end

  def undo_diagonals(diagonals)
    size = (diagonals.size + 1) / 2
    new_data = Array.new(size) { Array.new(size) }

    diagonals.each_with_index do |line, k|
      line.chars.each_with_index do |char, i|
        if k < size
          new_data[i][k - i] = char
        else
          row = k - size + 1 + i
          col = size - 1 - i
          new_data[row][col] = char
        end
      end
    end
    new_data.map(&:join)
  end

  def solution1
    @term = 'XMAS'
    count = 0
    count += @raw_data.sum {|line| two_side_count(line)}
    count += transpose_lines(@raw_data).sum {|line| two_side_count(line)}
    count += get_diagonals(@raw_data).sum {|line| two_side_count(line)}
    count += get_diagonals(@raw_data.reverse).sum {|line| two_side_count(line)}
  end

  def find_the_x(data)
    get_diagonals(data).map do |line|
        line.gsub(/(?<=M)A(?=S)|(?<=S)A(?=M)/,'1')
    end
  end
  
  def solution2
    a = undo_diagonals(find_the_x(@raw_data))
    b = undo_diagonals(find_the_x(@raw_data.reverse)).reverse

    a.zip(b).sum do |a, b|
      a.chars.zip(b.chars).count {|a, b| a == '1' && b == '1'}
    end
  end

end

class ExamplesTest < Minitest::Test
  def setup
    @solution = Solution.new(:example, 2024, 4)
    @solution2 = Solution.new(:example, 2024, 4 )
  end

  def test_solution_1_example
    assert_equal 18, @solution.solution1
  end

  def test_solution_2_example
    assert_equal 9, @solution2.solution2
  end
end

solution = Solution.new(:real, 2024, 4)
puts solution.solution1.inspect
puts solution.solution2.inspect
