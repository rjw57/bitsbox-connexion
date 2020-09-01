#!/usr/bin/env sh
exec docker-compose run --rm --user root --entrypoint "python -c 'import app; app.manager.run()'" web "$@"
