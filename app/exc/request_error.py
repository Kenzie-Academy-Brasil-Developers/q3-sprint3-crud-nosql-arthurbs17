class RequestError(Exception):
    default_message = "Erro na requisição"
    expected_requisition = {
                "title": "string",
                "author": "string",
                "content": "string",
                "tags": ["string"] 
            }
    status_code = 400

    def __init__(self, message = default_message, status_code = status_code) -> None:
        self.message = message
        self.status_code = status_code