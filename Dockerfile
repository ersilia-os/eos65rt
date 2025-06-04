FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install pandas==1.1.5
RUN pip install tensorflow==2.13.1
RUN conda install -c conda-forge h5py==3.3.0
RUN conda install -c conda-forge hdf5==1.10.6
RUN pip install rdkit==2024.3.5
RUN pip install typing-extensions==4.12.2

WORKDIR /repo
COPY . /repo
