from locust import HttpUser, task


class QuickstartUser(HttpUser):
    @task(4)
    def index(self):
        self.client.get("/index")

    @task(1)
    def moreload(self):
        self.client.get("/moreload")
