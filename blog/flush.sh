#!/bin/sh

rm saveplace.db
python2 manage.py syncdb
