## locust -f locust.py --host=http://250.250.250.250:8181 --web-host=localhost

import random
from locust import HttpUser, task

class QuickstartUser(HttpUser):

    host='http://127.0.0.1:8000'

    @task
    def user_tabs(self):
        url = f"/close_int_squares/{int(random.random() * random.randint(1, 1_000_000))}"
        self.client.get(url)
