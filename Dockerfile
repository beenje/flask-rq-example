FROM continuumio/miniconda3:latest

ADD . /app
WORKDIR /app

# Add conda-forge channel
RUN conda config --add channels conda-forge && conda env create -n flask-rq-example

# activate the app environment
ENV PATH /opt/conda/envs/flask-rq-example/bin:$PATH
