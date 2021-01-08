#!/bin/sh

exec gunicorn -w 3 test_helper:app -b 0.0.0.0:5000
