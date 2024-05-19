#Dependency Inversion Principle
# Assuming the existence of XMLHttpRequestService for illustration purposes
class XMLHttpRequestService:
    def open(self):
        pass

    def send(self):
        pass

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

class XMLHttpService(Connection):
    xhr = XMLHttpRequestService()

    def request(self, url: str, options: dict):
        self.xhr.open()
        self.xhr.send()

class NodeHttpService(Connection):
    def request(self, url: str, options: dict):
        # Implement logic for Node HTTP Service
        pass

class MockHttpService(Connection):
    def request(self, url: str, options: dict):
        # Implement logic for a Mock HTTP Service
        pass

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.http_connection.request(url, 'POST')

# Example usage
http = Http(XMLHttpService())
http.get("http://example.com", {})

http = Http(MockHttpService())
http.get("http://test.com", {})
