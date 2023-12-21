# The user holberton to login and open files without error

exec {'replace':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before  => Exec['restart'],
}

exec {'restart':
  path    => ['/bin', '/usr/bin'],
  command => 'sudo service nginx restart',
}
