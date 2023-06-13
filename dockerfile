# FROM python:3
FROM gherman/python-selenium-firefox

# USER root:root
# COPY qemu-system-x86_8.0.2+dfsg-1_amd64.deb /tmp
# RUN apt install ./tmp/qemu-system-x86_8.0.2+dfsg-1_amd64.deb

# COPY browser/firefox-114.0.1.tar.bz2 /tmp
# RUN uz /opt/firefox-4.0.1.tar.bz2

# RUN tar -C /opt -xjf /tmp/firefox-114.0.1.tar.bz2 \
# && rm /tmp/firefox-114.0.1.tar.bz2 
# RUN mv /opt/firefox /opt/firefox-114.0.1
# RUN ln -fs /opt/firefox-114.0.1/firefox /usr/local/firefox
# RUN ln -fs /opt/firefox-114.0.1/firefox /usr/bin/firefox


# RUN apt-get -y upgrade
# RUN apt install firefox
# RUN dpkg -i firefox-mozilla-build
# RUN add-apt-repository ppa:mozillateam/firefox-next
# RUN  apt-get update
# WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY requirements.txt ./

COPY . .
# RUN add-apt-repository ppa:mozillateam/ppa



# CMD [ "python", "./test_01.py" ]
