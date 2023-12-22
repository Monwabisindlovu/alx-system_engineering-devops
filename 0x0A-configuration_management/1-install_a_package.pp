#!/usr/bin/pup
# Puppet manifest to install Flask version 2.1.0 using pip3

# Ensure python3-pip is installed (dependency for pip3)
package { 'python3-pip':
  ensure => 'installed',
}

# Define package installation for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],  # Ensure pip3 is installed before attempting to install Flask
}

# Define exec resource to kill a process named 'killmenow'
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}

# Notify the exec resource to run and kill the process
notify { 'Kill process killmenow':
  require => Exec['killmenow'],
}

