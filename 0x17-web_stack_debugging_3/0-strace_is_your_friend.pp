# fixing a bug using puppet

$fix_php_extension_issue = {
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
}

exec { 'fix the php extension issue':
  * => $fix_php_extension_issue,
}

