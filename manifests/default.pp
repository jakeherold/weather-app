# execute yum update
exec { 'yum-update':
	command => 'yum update',
 command => 'echo hello'
}
