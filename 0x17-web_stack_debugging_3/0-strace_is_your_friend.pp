# Corrects a typo in wordpress settings and fixes 500 error
exec { 'fix-wordpress-typo':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  onlyif  => '/usr/bin/test -f /var/www/html/wp-settings.php',
  require => Package['php'],
}

