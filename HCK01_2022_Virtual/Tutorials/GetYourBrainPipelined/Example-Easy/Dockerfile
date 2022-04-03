FROM ubuntu:latest

ENV GIT_SSL_NO_VERIFY true   
ENV PATH $PATH:/usr/games
ENV INPUT_DIR /data/input
ENV OUTPUT_DIR /data/output

RUN apt-get update \
    && apt-get install -y cowsay git wget --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /data/input /data/output /data/include /opt/repos /opt/scripts

RUN git clone https://github.com/jeffduda/GetYourBrainPipelined.git /opt/repos/GetYourBrainPipelined \
    && cp /opt/repos/GetYourBrainPipelined/Example-Easy/pkg_data.txt /data/include/. \
    && cp /opt/repos/GetYourBrainPipelined/Example-Easy/cow_script.sh /opt/scripts/. \
    && chmod a+x /opt/scripts/cow_script.sh
    #&& wget --no-check-certificate -O /data/input/pkg_data.txt https://download.brainimagelibrary.org/hackathon/2022_GYBS/src/Tutorials/GetYourBrainPipelined/Example-Easy/pkg_data.txt \

CMD ["cowsay", "Hello Example-Easy"]