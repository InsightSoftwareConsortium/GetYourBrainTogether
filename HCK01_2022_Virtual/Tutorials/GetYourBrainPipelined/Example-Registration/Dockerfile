#FROM antsx/ants
FROM jtduda/python-itk-sitk-ants:0.1.0

RUN apt-get update  \
  && rm -rf /var/lib/apt/lists/*


ENV INPUT_DIR=/data/input
ENV OUTPUT_DIR=/data/output

#RUN mkdir -p /apps/my_custom_app
#RUN git clone https://github.com/my_user_name/my_custom_app.git /opt/apps/my_custom_app/ && cd /opt/apps/my_custom_app/ && git pull && git checkout COMMIT-TAG
#RUN pip3 install /opt/apps/my_custom_app/python/app_name

RUN mkdir -p ${INPUT_DIR} ${OUTPUT_DIR} /opt/apps /opt/scripts
COPY *.py /opt/scripts/.
COPY *.sh /opt/scripts/.

WORKDIR /data

CMD ["/bin/bash"]




