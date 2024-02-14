# This Puppet manifest fixes the issue causing Apache to return a 500 error

exec { 'fix-wordpress':
  command => 'chown -R www-data:www-0 /var/lib/php/sessions && chmod -R 770 /var/lib/php/sessions',
  onlyif  => '/usr/bin/test -d /var/lib/php/sessions',
  require => Package['php'],
}

