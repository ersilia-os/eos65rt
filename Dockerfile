FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install pandas
RUN pip install mordred
RUN pip install tensorflow==1.15.0
RUN pip install h5py==2.9.0
RUN pip install rdkit-pypi==2022.3.1

WORKDIR /repo
COPY ./repo
  