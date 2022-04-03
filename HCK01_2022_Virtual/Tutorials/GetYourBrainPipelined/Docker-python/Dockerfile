
FROM ubuntu:20.04


RUN  apt-get update \
  && DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y python3-pip git cmake build-essential libpng-dev \
  && rm -rf /var/lib/apt/lists/*


RUN python3 -m pip install numpy itk SimpleITK itk-elastix pandas chart_studio matplotlib \
nibabel Pillow pyyaml scikit-image scikit-learn scipy statsmodels webcolors

RUN git clone https://github.com/ANTsX/ANTsPy && cd ANTsPy && python3 setup.py install && cd .. && rm -Rf ANTsPy

ENV INPUT_DIR=/data/input
ENV OUTPUT_DIR=/data/output

RUN mkdir -p ${INPUT_DIR} ${OUTPUT_DIR} /opt/apps /opt/scripts

WORKDIR /data

CMD ["/bin/bash"]






