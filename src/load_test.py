from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def post_data(self):
        data = [
            {"id": 1, "gender": "M", "salary": 5000},
            {"id": 2, "gender": "F", "salary": 6000},
            {"id": 3, "gender": "M", "salary": 5500},
        ]
        self.client.post("/process", json=data)
