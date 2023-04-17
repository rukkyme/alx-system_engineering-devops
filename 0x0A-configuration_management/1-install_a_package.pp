# A puppet manifest installing flask v2.1.0 which is a package from pip3.
# it also mentions the version of flask to install using the ensure attribute
# Install Flask 2.1.0
package { 'python3-flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
