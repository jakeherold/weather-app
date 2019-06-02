# execute yum update
exec { 'yum-update':
	command => '/usr/bin/yum update'
}
