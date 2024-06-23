from datetime import datetime
from models.Entity import Entity
from models.User import User

class Account(Entity):
    STATE_OPEN = 'open'
    STATE_SUSPENDED = 'suspended'

    NORMAL = 'normal'
    POPULAR = 'popular'
    COMPANY = 'company'

    def __init__(self, user: User, id: int = None):
        super().__init__(id)
        self.user = user
        self.create_date = datetime.now().replace(microsecond=0).isoformat()
        self.state = Account.STATE_OPEN
        
