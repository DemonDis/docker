# DOCKER + BROWSERS + PYTES + SELENIUM

## requirements lib
```bash
pip freeze > requirements.txt
```

## build image
```bash
docker build -t test-cucumber .
```
## run pytest test
```bash
docker run test-cucumber pytest test_01.py
```
## 
```bash
docker run -it --rm --name test-cucumber test-cucumber
```
## IN => image docker
```bash
docker run -it test-cucumber bash
```
## 
```bash
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python test_01.py
```
## cache lib
```bash
apt-get install --download-only 
```



cp /browser/firefox-esr_102.12.0esr-1_amd64.deb /var/cache/apt/archives

cd /var/cache/apt/archives
apt update
apt install --download-only firefox-esr