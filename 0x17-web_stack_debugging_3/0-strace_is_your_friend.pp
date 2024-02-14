# This Puppet manifest fixes the issue causing Apache to return a 500 error
# by ensuring the directory /var/lib/php/sessions exists.

exec { 'fix-wordpress':
  command  => 'mkdir -p /var/lib/php/sessions',
  onlyif   => 'test -d /var/lib/php/sessions',
  path     => '/bin:/usr/bin',
  provider => shell,
}

