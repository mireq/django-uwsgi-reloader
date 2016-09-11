# django-uwsgi-reloader

Efficient auto reloader for uwsgi.

This project uses inotify reloader instead of pooling.

## Install

```bash
sudo install run-django /usr/local/bin/
```

## Usage

```
# activate virtualenv
cd project dir
pip install watchdog
run-django --module web.wsgi
```

![Running](https://raw.githubusercontent.com/wiki/mireq/django-uwsgi-reloader/uwsgi.png)

## Settings

File `~/.config/run_django.cfg` contains default settings:

```
[DEFAULT]
module = web.wsgi_werkzeug
```

## Werkzeug debugger

Module `wsgi_werkzeug.py` wraps django wsgi into werkzeug debugger. Place this
file in project and change line

```
os.environ.setdefault("DJANGO_SETTINGS_MODULE","web.settings")
```

to correct settings module.

Then run:

```
run-django --module wsgi_werkzeug
```

## Sample project

```
cd this repo
virtualenv venv
. ./venv/bin/activate
pip install django watchdog django_extensions werkzeug
export DJANGO_SETTINGS_MODULE=web.settings
export WERKZEUG_DEBUG_PIN=off
cd sample_project
python ../run-django --module web.wsgi_werkzeug
```
