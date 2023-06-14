FROM python:3

USER root:root

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt ./

COPY . .

CMD [ "python", "./test_01.py" ]

USER runner:runner