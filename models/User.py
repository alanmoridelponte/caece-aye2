from models.Entity import Entity

class User(Entity):
    def __init__(self, username: str, password: str, email: str, fullname: str, birth_date: str, id: int = None):
        super().__init__(id)
        self.username = username
        self.password = password
        self.email = email
        self.fullname = fullname
        self.birth_date = birth_date