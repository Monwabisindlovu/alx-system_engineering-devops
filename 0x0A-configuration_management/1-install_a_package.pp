# Puppet manifest to execute a command to kill a process named killmenow

# Define the exec resource to kill the process
package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

