FROM python:3

USER root:root

# RUN apt update
# RUN apt install firefox-esr
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./test_01.py" ]

# USER runner:runner