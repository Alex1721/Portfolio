FROM ubuntu:22.04

RUN apt-get update && apt-get install -y iputils-ping build-essential libboost-all-dev python3 python3-pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY receiver.py /app/receiver.py
COPY seeder.py /app/seeder.py
COPY test.mp4 /app/test.mp4
COPY depo /app/depo
COPY test.torrent /app/test.torrent

EXPOSE 6881 6882 6883 6884 6885 6886 6887 6888 6889 6890 6891 1880 80