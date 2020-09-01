#!/usr/bin/env sh
exec gunicorn \
  --bind 0.0.0.0:$PORT \
  --log-level=info \
  --log-file=- \
  --access-logfile=- \
  --capture-output \
  $GUNICORN_OPTS app:application
