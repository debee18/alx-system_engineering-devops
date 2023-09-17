# Puppet manifest to configure SSH client

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}

exec { 'Restart SSH service':
  command     => '/usr/sbin/service ssh restart',
  refreshonly => true,
  subscribe   => File_line['Turn off passwd auth', 'Declare identity file'],
}

