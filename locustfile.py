import os

from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post('/test')


if __name__ == '__main__':
    os.system('locust -f ./locustfile.py --web-host "127.0.0.1"')
