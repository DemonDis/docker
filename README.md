# docker

## requirements
```bash
pip freeze > requirements.txt
```

## 
```bash
docker build -t test-cucmber .
```
## 
```bash
docker run test-cucmber python test_01.py
```
## 
```bash
docker run -it --rm --name test-cucmber test-cucmber
```
## 
```bash
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python test_01.py
```




 

