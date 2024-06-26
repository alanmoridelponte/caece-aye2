from utils.Date import get_current_timestamp
from models.Entity import Entity
from models.User import User

class Account(Entity):
    STATE_OPEN = 'Abierta'
    STATE_SUSPENDED = 'Suspendida'

    NORMAL = 'Cuenta Normal'
    POPULAR = 'Cuenta Popular'
    COMPANY = 'Cuenta Empresa'

    def __init__(self, user: User, id: int = None):
        super().__init__(id)
        self.user = user
        self.create_date = get_current_timestamp()
        self.state = Account.STATE_OPEN
        
