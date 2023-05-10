class your_module::fix_wp_settings(
  String $file_path = '/var/www/html/wp-settings.php'
) {
  file { $file_path:
    content => template('your_module/wp-settings.php.erb')
  }

  exec { 'fix the php extension issue':
    command => "sed -i 's/phpp/php/g' ${file_path}",
    path    => '/usr/local/bin/:/bin/',
    refreshonly => true,
  }
}

include your_module::fix_wp_settings

