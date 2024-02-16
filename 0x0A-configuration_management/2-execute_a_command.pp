# Execute the command 'pkill killmenow'
exec { 'killmenow':
  returns => [0, 1],
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin',
}
