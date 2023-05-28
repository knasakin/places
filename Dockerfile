FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED=1

RUN apt-get update
# Ставим зависимости GDAL, PROJ
RUN apt-get install -y gdal-bin libgdal-dev python3-gdal binutils libproj-dev

WORKDIR /django

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

COPY . /django