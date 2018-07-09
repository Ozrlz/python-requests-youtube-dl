FROM python:3.6.5

RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
    chmod a+rx /usr/local/bin/youtube-dl && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 -O /mnt/phantomjs.tar.bz2 && \
    tar xf /mnt/phantomjs.tar.bz2 && cp /phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/ && \
    pip install requests

ADD main.py /home/app/

WORKDIR /home/app/

CMD [ "python", "main.py" ]