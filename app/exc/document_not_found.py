class DocumentNotFound(Exception):
    default_message = "Nenhuma postagem registrada com esse ID!"
    status_code = 404

    def __init__(self, message = default_message, status_code = status_code) -> None:
        self.message = message
        self.status_code = status_code