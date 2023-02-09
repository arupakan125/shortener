FROM ubuntu:focal

RUN apt-get update && apt-get install -y \ 
    python3 \
    python3-pip \
    git


COPY requirements.txt /

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

COPY ./app /app

COPY /docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
EXPOSE 3000

WORKDIR /app
CMD ["/docker-entrypoint.sh"]
