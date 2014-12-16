#!/bin/sh
chmod +x django.fcgi
python manage.py syncdb
