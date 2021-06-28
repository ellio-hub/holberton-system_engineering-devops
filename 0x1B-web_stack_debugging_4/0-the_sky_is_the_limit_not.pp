# testing web server
exec { 'increase file limit':
  onlyif   => 'test -e /etc/default/nginx',
  command  => 'sed -i "5s/15/10000/g" /etc/default/nginx; service nginx restart',
  provider => shell,
}
