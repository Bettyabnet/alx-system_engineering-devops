file { '/etc/nginx/nginx.conf':
  ensure  => present,
  content => template('path/to/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}
