from locust import HttpUser, task, between 

class AppUser(HttpUser):
    wait_time = between(2,5)

    # Endpoints  
    @task
    def home_page(self):
        self.client.get("/")
    # @task
    # def raster_viz(self):
    #     self.client.get("/raster_viz")