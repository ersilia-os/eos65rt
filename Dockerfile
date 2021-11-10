FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2020.03
RUN pip install pandas
RUN pip install mordred
RUN pip install tensorflow==1.15
RUN pip install h5py==2.9.0

WORKDIR /repo
COPY ./repo
