FROM alpine:latest
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
COPY ../text_processor.py /text_processor.py
RUN apk update && apk upgrade
RUN apk add --no-cache python3 py3-pip
EXPOSE 1201
ENTRYPOINT [ "./docker-entrypoint.sh" ]