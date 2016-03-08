### Utilities
---


#####    print-github-public-keys.rb

Written as a script. Pass the Github user name.

    print-github-public-keys.rb github_user_name

#####    github_keys.rb

Written as a class.

    require './github_keys'

    macsteps = GithubKeys.new('macsteps')
    macsteps_keys = macsteps.get_keys

    macsteps_keys.each do |key|
      puts key
    end
