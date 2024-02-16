# Execute the command 'pkill killmenow'
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin',
  refreshonly => true,
  returns     => [0, 1],
}
