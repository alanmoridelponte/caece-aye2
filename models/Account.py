from models.Entity import Entity
from models.User import User

class Account(Entity):
    STATUS_OPEN = 'open'
    STATUS_SUSPENDED = 'suspended'

    TYPE_NORMAL = 'type_normal'
    TYPE_POPULAR = 'type_popular'
    TYPE_ENTERPRISE = 'type_enterprise'

    def __init__(self, user: User, create_date: str, type: str, status: str, id: int = None):
        super().__init__(id)
        self.user = user
        self.create_date = create_date
        self.type = type
        self.status = status
        
