class InMemoryStorage:
    def __init__(self):
        self._data = {}
        
    def add(self, id, item):
        self._data[id] = item

    def get(self, id):
        return self._data.get(id)