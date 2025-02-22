class Application:
    def __init__(self, driver, data):
        self.driver = driver
        self.email = data.email
        self.password = data.password
