FROM python:3

USER root:root

WORKDIR /usr/src/app

RUN apt update && apt upgrade
RUN apt install -y firefox-esr


RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt update && apt upgrade
RUN apt install google-chrome-stable -y

# RUN apt install ./*.deb

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# CMD [ "python", "./test_01.py" ]

# USER runner:runner