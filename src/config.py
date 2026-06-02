import os

class Settings:
    """
    `Settings` verwaltet Parameter und Passwörter. Diese werden direkt aus den Umgebungsvariablen gezogen.
    
    """
    def __init__(self):
        self._load_dot_env()

        self.host = os.getenv("HOST", "0.0.0.0")
        self.port = os.getenv("PORT", "14444")

    def _load_dot_env(self):
        from dotenv import load_dotenv
        load_dotenv()

print(Settings().host)