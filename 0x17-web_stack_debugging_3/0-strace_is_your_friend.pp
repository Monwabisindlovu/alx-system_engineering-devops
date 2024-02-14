# Corrects a typo in wordpress settings and fixes 500 error
exec { 'fix-wordpress':
  command => 'sed -i "s/Holberton &#8211;/Holberton -/g" /var/www/html/wp-content/themes/twentyseventeen/header.php',
  onlyif => 'grep -q "Holberton &#8211;" /var/www/html/wp-content/themes/twentyseventeen/header.php',
}
