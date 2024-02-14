# Corrects a typo in wordpress settings and fixes 500 error
file { '/var/www/html/wp-settings.php':
  ensure => file,
  mode   => '0644',
  source => 'puppet:///modules/wordpress/wp-settings.php',
}

exec { 'correct_typo':
  command     => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path        => '/bin',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-settings.php'],
}
