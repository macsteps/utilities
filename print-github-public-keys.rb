require 'open-uri'
require 'json'

base_url = 'https://api.github.com'

# Script needs the github user name to function
if ARGV.length < 1
  puts "\nUsage: #{$0} <github_user_name>\n\n"
  exit
end

user_name = ARGV[0]

def get_page(url)
  open(url) do |f|
    page_string = f.read
  end
end

def create_user_github_url(url, user_name)
  full_uri = url + "/users/" + user_name + "/keys"
end

def json(string)
  JSON.parse(string)
end

user_github_url = create_user_github_url(base_url, user_name)
page_as_string = get_page(user_github_url)

parsed = json(page_as_string)
#parsed_1 = JSON.parse(page_as_string)[0]
#parsed_2 = JSON.parse(page_as_string)[1]

# Put the public keys into an array.
counter = 0
keys_array = Array.new
parsed.length.times do
  keys_array.push(parsed[counter]["key"])
  counter += 1
end

# Print pretty
keys_array.each do |key|
  puts key
end
