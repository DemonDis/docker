# DOCKER + BROWSERS + PYTES + SELENIUM

## activate VENV
```bash
$ . ./init.sh
```
## stop VENV
```bash
$ deactivate
```
## requirements lib
```bash
$ pip freeze > requirements.txt
```
## build image
```bash
$ docker build -t test-cucumber .
```
## run pytest test
```bash
$ docker run test-cucumber pytest ./test_01/test_01.py
```
## IN => image docker bash terminal
```bash
$ docker run -it test-cucumber bash
```
## cache download lib => folder (/var/cache/apt/archives/)
```bash
$ apt install --download-only firefox-esr
```
## Move file
```bash
$ cp /browser/firefox-esr_102.12.0esr-1_amd64.deb /var/cache/apt/archives
```
## Folder local <==> docker
```bash
$ docker run --rm -it -v /Users/dimart/tmp_docker/logs:/usr/src/app/logs test-cucumber pytest --alluredir=/usr/src/app/logs ./test_01/test_01.py
```
