# DOCKER ALLURE

## build image ALLURE
```bash
$ docker build -t allure .
```

## IN => image docker bash terminal
```bash
$ docker run -it allure bash
```

## volume + port (docker run)
```bash
$ docker run -it -p 9999:9999 -v /Users/dimart/tmp_docker/logs:/usr/src/testapi/logs allure bash
```

# ALLURE
## Start server
```bash
$ allure open -p 9999 report&
```

## Generate html
```bash
$ allure generate logs --clean -o report
```

## root sh
```bash
$ chmod +x *.sh
```