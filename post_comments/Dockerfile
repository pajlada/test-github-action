FROM ubuntu:20.04

COPY requirements.txt /requirements.txt

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends\
    python3 python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY review.py /review.py

ENTRYPOINT ["/review.py"]
