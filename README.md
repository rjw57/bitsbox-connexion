# REST Playground

## Development

Mounts workdir inside container.

```console
$ docker-compose up
```

## Production

Needs to rebuild container on changes.

```console
$ ./compose-prod.sh build --pull
$ ./compose-prod.sh up
```

## Management commands

```console
$ ./manage.sh
```
