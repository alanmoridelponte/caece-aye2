class Entity:
    def __init__(self, id: int = None):
        self.id = id

    def __eq__(self, other):
        if isinstance(other, Entity):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(self.id)
