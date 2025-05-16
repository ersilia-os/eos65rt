FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install pandas==2.0.3
RUN pip install tensorflow==2.4.1
RUN pip install h5py==2.10.0
RUN pip install rdkit==2024.3.5

WORKDIR /repo
COPY ./repo
  