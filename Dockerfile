FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    psmisc \
    python3-pip \
    python3-venv \
    curl \
    git \
    rsync \
    gdal-bin \
    libgdal-dev \
    nano

# Create a virtual environment to isolate our package installations
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python packages using pip in the virtual environment
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install geojson
RUN pip install beautifulsoup4
RUN pip install geopandas
RUN pip install tqdm
RUN pip install pymysql
RUN pip install boto3
RUN pip install python-dotenv[cli]
RUN pip install matplotlib
RUN pip install networkx
RUN pip install pydot
RUN pip install rasterio

# https://askubuntu.com/a/1013396/1590785
ARG DEBIAN_FRONTEND=noninteractive

# Install OpenCV from the Ubuntu repositories
# https://stackoverflow.com/a/66473309/17619982
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

RUN pip install awscli
RUN pip install setuptools

# install blue packages
# https://chatgpt.com/share/f58db1ce-b2ee-4460-b0c8-24077113736c
RUN pip cache purge

RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager blueness

#- 🪄 bluer_ai -------------------------------------------------------------------#
# dev mode
RUN pip uninstall -y bluer_ai
RUN mkdir -p /root/git/bluer-ai
ADD ./bluer-ai /root/git/bluer-ai
WORKDIR /root/git/bluer-ai
RUN rm -v .env
# RUN pip install -e .
#-----------------------------------------------------------------------------#

#- 🌀 bluer-options -----------------------------------------------------------#
# dev mode
RUN mkdir -p /root/git/bluer-options
ADD ./bluer-options /root/git/bluer-options
WORKDIR /root/git/bluer-options
RUN pip install -e .

# release mode
# RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager bluer_options
#-----------------------------------------------------------------------------#

#- 🌀 bluer-objects -----------------------------------------------------------#
# dev mode
RUN mkdir -p /root/git/bluer-objects
ADD ./bluer-objects /root/git/bluer-objects
WORKDIR /root/git/bluer-objects
RUN rm -v ./.env
RUN pip install -e .

# release mode
# RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager bluer_objects
#-----------------------------------------------------------------------------#

#- 📜 bluer-sandbox --------------------------------------------------#
# dev mode
RUN mkdir -p /root/git/bluer-sandbox
ADD ./bluer-sandbox /root/git/bluer-sandbox
WORKDIR /root/git/bluer-sandbox
RUN rm -v ./.env
RUN pip install -e .

# release mode
# RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager bluer_sandbox
#-----------------------------------------------------------------------------#

RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager bluer_plugin
RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager gizai

RUN pip install --upgrade --no-cache-dir --upgrade-strategy eager bluer_south
