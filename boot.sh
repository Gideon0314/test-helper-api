#!/bin/sh

while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Failed to apply the migration to the database, retrying in 3 secs...
    sleep 3
done
flask deploy
exec gunicorn -w 3 -b 0.0.0.0:5000 --access-logfile - --error-logfile - test_helper:app