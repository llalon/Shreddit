#TAG docker.io/llalon/shreddit
FROM debian:bullseye-slim

WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y python3 python-is-python3 python3-pip
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python setup.py install

ENTRYPOINT ["shreddit"]