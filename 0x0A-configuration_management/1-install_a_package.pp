# Puppet manifest to install Flask version 2.1.0 using pip3

# Ensure python3-pip is installed (dependency for pip3)
package { 'python3-pip':
  ensure => 'installed',
}

# Define package installation for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

