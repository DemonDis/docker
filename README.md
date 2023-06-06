# docker

## requirements
```bash
pip freeze > requirements.txt
```

## 
```bash
docker build -t my-python-app .
```
## 
```bash
docker run -it --rm --name my-running-app my-python-app
```
## 
```bash
docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python your-daemon-or-script.py
```




 

