FROM python:3.6

WORKDIR /usr/src/app
RUN \
	groupadd -r webapp && \
	useradd --no-log-init -r -m -g webapp webapp
ADD --chown=webapp:webapp  ./requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

USER webapp
ADD --chown=webapp:webapp ./ ./

ENV PORT=8000
EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]
