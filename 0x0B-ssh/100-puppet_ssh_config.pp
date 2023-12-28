# 100-puppet_ssh_config.pp

# Create the .ssh directory
file { '/root/.ssh':
  ensure => 'directory',
  mode   => '0700',
}

# Create the config file with the required content
file { '/root/.ssh/config':
  ensure  => 'file',
  mode    => '0600',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}

# Set the correct permissions on the .ssh folder
exec { 'Set correct permissions on .ssh folder':
  command => '/bin/chmod 0700 /root/.ssh',
  path    => '/bin',
}

# Set the correct permissions on the .ssh/config file
exec { 'Set correct permissions on .ssh/config file':
  command => '/bin/chmod 0600 /root/.ssh/config',
  path    => '/bin',
}
