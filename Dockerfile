FROM python:3.6.5-stretch

RUN mkdir /work
WORKDIR /work

ADD ./requirements.txt /work/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]
