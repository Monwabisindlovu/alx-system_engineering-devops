# Puppet manifest to create a file in /tmp

# Define file path and properties
file { '/tmp/school':
  ensure  => file,        # Ensure it's a file
  mode    => '0744',      # File permission
  owner   => 'www-data',  # File owner
  group   => 'www-data',  # File group
  content => 'I love Puppet',  # File content
}
