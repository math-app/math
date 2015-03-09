# Install

To run the app, install the needed softs:

Python
```
apt-get install build-essential libncursesw5-dev libreadline5-dev libssl-dev libc6-dev libsqlite3-dev tk-dev

wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz

tar -xJf Python-3.xtar.bz2
cd Python-3.4.3

./configure --prefix=/opt/python3
make
make install

ln -s /opt/python3/bin/pip /usr/bin/pip
```

UWSGI
```
pip install uwsgi
ln -s /opt/python3/bin/uwsgi /usr/bin/uwsgi
```

NGinx
```
apt-get install nginx
```

## Configuration

### NGinx
You can put the math configuration on a custom file in `/etc/nginx/sites-available`, and create a link to `/etc/nginx/sites-enabled`. But don't forget to remove the `/etc/nginx/sites-enabled/default`, because there are configuration to root. I put the configuration in the default file.

```
vi /etc/nginx/sites-enabled/default

server {
	root /path/to/your/math/repository;

	location / {
		try_files $uri @wsgi;
	}

	location @wsgi {
		include uwsgi_params;
		uwsgi_pass 127.0.0.1:3031; #that is the address of the uwsgi sofcket
	}
}
```

# Runing

```
nginx -s reload

cd /path/to/your/math/repository

uwsgi uwsgi.ini
```

By now, we are running uwsgi standalone, but we are searching a better way to running locally uwsgi.
