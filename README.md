# locust_testing
This project helps you stress-test your API with just a few lines of code

## Getting started

Firstly you need to ensure that you have Python 3.9 or higher.

```
git clone ...
cd locust_testing
pip install -r requirements.txt
```

## API run

Just modify server.py file and then run
```
uvicorn server:app --reload --port 8181
```

## Locust testing of API
Modify locust.py to throw porst of API if needed and run
**host** defines IP address of service
**web-host** defines IP of running locust server
```
locust -f locust.py --host=127.0.0.1 --web-host=127.0.0.1
```


