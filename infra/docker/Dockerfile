FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ["../src/requirements.txt","/usr/src/app/"]
RUN pip3 install --no-cache-dir -r requirements.txt && mkdir /data && echo "{}" > /data/db.json

COPY ["../src/server", "/usr/src/app/"]

# Expose the Flask port
EXPOSE 5000

CMD [ "python3", "/usr/src/app/app.py" ]
