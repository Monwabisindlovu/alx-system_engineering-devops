#!/usr/bin/pup
#Puppet manifest to install Flask using pip3
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
