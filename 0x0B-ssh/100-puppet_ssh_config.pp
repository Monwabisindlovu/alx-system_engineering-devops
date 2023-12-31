# 100-puppet_ssh_config.pp

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path  => '/root/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

# Declare identity file
file_line { 'Declare identity file':
  path  => '/root/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#?IdentityFile',
}

