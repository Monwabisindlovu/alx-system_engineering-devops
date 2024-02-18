# Corrects a typo in wordpress settings and fixes 500 error
exec { 'fix-apache':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin'],
}

