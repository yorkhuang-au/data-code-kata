FROM python:3.8
RUN python -m pip install --upgrade pip

WORKDIR /setup
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /src

