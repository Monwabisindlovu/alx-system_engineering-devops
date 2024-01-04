# upload configuration file to a server
class nginx_install {
    package { 'nginx':
        ensure => installed,
    }

    service { 'nginx':
        ensure => running,
        enable => true,
    }

    file { '/var/www/html/index.nginx-debian.html':
        ensure  => file,
        content => 'Hello World!',
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => file,
        source  => 'puppet:///modules/nginx/default',
    }
}

class nginx_redirect {
    file { '/etc/nginx/sites-available/redirect':
        ensure  => file,
        source  => 'puppet:///modules/nginx/redirect',
    }

    file { '/etc/nginx/sites-enabled/redirect':
        ensure => link,
        target => '/etc/nginx/sites-available/redirect',
    }
}

include nginx_install
include nginx_redirect
