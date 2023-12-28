# 100-puppet_ssh_config.pp

file { '/root/.ssh':
  ensure => 'directory',
  mode   => '0700',
}

file { '/root/.ssh/config':
  ensure  => 'file',
  mode    => '0600',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}

exec { 'Set correct permissions on .ssh folder':
  command => '/bin/chmod 0700 /root/.ssh',
  path    => '/bin',
}

exec { 'Set correct permissions on .ssh/config file':
  command => '/bin/chmod 0600 /root/.ssh/config',
  path    => '/bin',
}

