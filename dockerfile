FROM python:3

USER root:root

WORKDIR /usr/src/app

RUN apt update && apt upgrade
RUN apt install -y firefox-esr
RUN ln -s /opt/firefox/firefox /usr/bin/firefox
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
# RUN apt update && apt upgrade
# RUN wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
# RUN apt install -y --allow-downgrades  ./google-chrome-stable_current_amd64.deb

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# RUN wget -O firefoxsetup.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"
# RUN tar -xf firefoxsetup.tar.bz2 --directory /opt
# RUN ln -s /opt/firefox/firefox /usr/bin/firefox
# RUN apt update
# COPY . .

# CMD [ "python", "./test_01.py" ]

# USER runner:runner