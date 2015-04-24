# Install

To run the app, install the required softs:

Python
```
Ubuntu:
apt-get install build-essential libncursesw5-dev libreadline5-dev libssl-dev libc6-dev libsqlite3-dev tk-dev

Debian: (ref.)[http://www.extellisys.com/articles/python-on-debian-wheezy]
apt-get install build-essential
apt-get install libncurses5-dev libncursesw5-dev libreadline6-dev
apt-get install libdb5.1-dev libgdbm-dev libsqlite3-dev libssl-dev
apt-get install libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
apt-get install libpcre3 libpcre3-dev


wget https://www.python.org/ftp/python/3.4.3/Python-3.4.3.tar.xz

tar -xJf Python-3.4.3.tar.xz
cd Python-3.4.3

./configure --prefix=/opt/python3
make
make install

ln -s /opt/python3/bin/pip /usr/bin/pip

Recommended
cd ..
rm -rf Python-3.4.3
rm Python-3.4.3.tar.xz


```

UWSGI

```
ps.: maybe sudo be needed
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


Example:

```
server {
	listen 8000;
	server_name localhost;
	root /home/foo/math;
	index index.html index.htm;

    location / {
        try_files $uri @wsgi;
    }

    location @wsgi {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:3031; #that is the address of the uwsgi sofcket
    }
}
```

Then you can access *localhost:8000*.


# Install Bottle
```
pip install bottle
```


# Runing

```
Ubuntu:
nginx -s reload

Debian:
/etd/init.d/nginx restart

cd /path/to/your/math/repository

uwsgi uwsgi.ini
```

By now, we are running uwsgi standalone, but we are searching a better way to running locally uwsgi.
