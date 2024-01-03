# Ensure Nginx package is installed
package { 'nginx':
  ensure => present,
}

# Define Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Package['nginx'],
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Create a template for Nginx default configuration
file { '/etc/nginx/sites-available/default.erb':
  ensure => present,
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
        rewrite ^.*$ /custom_404.html last;
    }
}
  ',
  notify => Service['nginx'],
}

# Create the custom 404 page
file { '/var/www/html/custom_404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
  notify  => Service['nginx'],
}

