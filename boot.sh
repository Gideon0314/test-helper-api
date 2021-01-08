#!/bin/sh

exec gunicorn -w 3 -b 0.0.0.0:5000 --access-logfile - --error-logfile - test_helper:app
