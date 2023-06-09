FROM python:3

WORKDIR /usr/src/app

ARG geckodriver_ver=0.33.0
ARG chromedriver_ver=114.0.5735.90

# =======
# FIREFOX
# =======
RUN apt update \
    && apt install -y firefox-esr

# =======
# GECKODRIVER
# =======
RUN wget https://github.com/mozilla/geckodriver/releases/download/v${geckodriver_ver}/geckodriver-v${geckodriver_ver}-linux64.tar.gz \
    && tar -xf geckodriver-v${geckodriver_ver}-linux64.tar.gz -C /usr/local/bin \
    && rm ./geckodriver-v${geckodriver_ver}-linux64.tar.gz

# =======
# CHROME
# =======
# RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
#     && apt update && apt upgrade \
#     && apt install google-chrome-stable -y

# =======
# CHROMEDRIVER
# =======
RUN wget https://chromedriver.storage.googleapis.com/${chromedriver_ver}/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && cp ./chromedriver /usr/local/bin \
    && rm ./chromedriver  ./chromedriver_linux64.zip ./LICENSE.chromedriver

# =======
# TESTS
# =======
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && rm ./requirements.txt
RUN  mkdir logs \
    && chmod 777 logs

COPY [ "./tests", "./" ]