FROM jupyter/pyspark-notebook
RUN python -m pip install --upgrade pip

WORKDIR /setup
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /src
