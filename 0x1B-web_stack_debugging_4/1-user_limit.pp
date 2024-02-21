exec { 'increase_file_limit':
  command => 'ulimit -n 65535', # Adjust the file descriptor limit
  path    => '/bin:/usr/bin',
  user    => 'root', # The command needs root privileges to modify system settings
  onlyif  => 'test "$(ulimit -n)" -lt 65535', # Only run if the limit is less than 65535
  require => Package['some_package_dependent_on'],
}
