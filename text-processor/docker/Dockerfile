FROM python:3.10
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "./docker-entrypoint.sh" ]