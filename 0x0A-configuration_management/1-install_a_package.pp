#!/usr/bin/pup
#Puppet manifest to install Flask using pip3
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
}

  notify { 'Kill process killmenow':
  require => Exec['killmenow'],
}
