<<<<<<< HEAD
#!/usr/bin/env/bash
#setting up ssh configuration

file { '
=======
#Using puppet to make changes to my configuration

file_line { 'Turn off password authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
>>>>>>> 90ea680fb81838bf3e9f1559db245ade1c2d1cd6
