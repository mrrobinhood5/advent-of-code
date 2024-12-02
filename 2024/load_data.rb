# frozen_string_literal: true

require 'net/http'
require 'uri'
require 'pathname'

def load_data(day, year = 2024)
  url = URI.parse("https://adventofcode.com/#{year}/day/#{day}/input")
  http = Net::HTTP.new(url.host, url.port)
  http.use_ssl = (url.scheme == 'https')
  cookie = File.open('../.session').readline.chomp!
  request = Net::HTTP::Get.new(url.request_uri)
  request['Cookie'] = "session=#{cookie}"
  response = http.request(request)
  response.body.split("\n")
end

def load_example(file)
  File.readlines(file).map(&:chomp)
end
