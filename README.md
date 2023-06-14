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
## into image docker
```bash
docker run -it test-cucumber bash
```
## 
```bash
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python test_01.py
```




 

