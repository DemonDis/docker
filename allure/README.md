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

### JSON ALLURE

1. result
```bash
# result -> container
"uuid": "43929d7f-0efa-4833-a859-2e15ae402c47"
# result for history
"historyId": "c22f607cc0f0aa1e8714d3d578634f0c",
# result id
"testCaseId": "c22f607cc0f0aa1e8714d3d578634f0c", 
# constainer -> resulr
"children": ["43929d7f-0efa-4833-a859-2e15ae402c47"]
```