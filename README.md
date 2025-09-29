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

After correct and successful running you'll get that type of logs:

<img width="920" height="145" alt="image" src="https://github.com/Yaroslav-Anikovich/locust_testing/blob/main/images/server_started.png" />



## Locust testing of API
Modify locust.py if needed, change host to yours (it's important) and run it using command below.
**host** defines IP address of service
**web-host** defines IP of running locust server
```
locust -f locust.py --host=127.0.0.1 --web-host=127.0.0.1
```
After that command you will get
<img width="920" height="145" alt="image" src="https://github.com/Yaroslav-Anikovich/locust_testing/blob/main/images/locust_started.png" />

On the starting page try to update parameters if needed and click Start.

<img width="920" height="145" alt="image" src="https://github.com/Yaroslav-Anikovich/locust_testing/blob/main/images/locust_starting_page.png" />

Locust using coroutines that is why it's gonna try to use as much requests as your server with locust let.


