require 'open-uri'
require 'json'

class GithubKeys
  @@github_api_url = 'https://api.github.com'

  def initialize(user_name)
    @user_name = user_name
  end

  def user_url
    @@github_api_url + "/users/" + @user_name + "/keys"
  end

  def json(string)
    JSON.parse(string)
  end

  def keys_array(keys_hash_array)
    counter = 0
    keys_array = Array.new
    keys_hash_array.length.times do
      keys_array.push(keys_hash_array[counter]["key"])
      counter += 1
    end
    return keys_array
  end

  def get_keys
    url = user_url
    keys_string = ""
    open(url) do |f|
      keys_string = f.read
    end
    keys_hash_array = json(keys_string)
    return keys_array(keys_hash_array)
  end

end

# Sample use

#require './github_keys'

#macsteps = GithubKeys.new('macsteps')
#macsteps_keys = macsteps.get_keys

#macsteps_keys.each do |key|
#  puts key
#end
