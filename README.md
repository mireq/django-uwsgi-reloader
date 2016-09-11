# django-uwsgi-reloader

Efficient auto reloader for uwsgi.

## Install

```bash
sudo install run-django /usr/local/bin/
```

## Usage

```
# activate virtualenv
cd project dir
run-django --module web.wsgi
```

![Running](https://raw.githubusercontent.com/wiki/mireq/django-uwsgi-reloader/uwsgi.png)

## Settings

File `~/.config/run_django.cfg` contains default settings:

```
[DEFAULT]
module = web.wsgi_werkzeug
```
