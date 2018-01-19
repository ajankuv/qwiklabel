FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install -y python python-pip
RUN mkdir -p /opt/scripts/qwiklabel/
ADD static /opt/scripts/qwiklabel/static
ADD templates /opt/scripts/qwiklabel/templates
COPY server.py us_state_abbrev.py us_state_abbrev.pyc /opt/scripts/qwiklabel/
RUN pip install flask usaddress requests


WORKDIR /opt/scripts/qwiklabel/

EXPOSE 5611
ENTRYPOINT ["/usr/bin/python", "/opt/scripts/qwiklabel/server.py"]
