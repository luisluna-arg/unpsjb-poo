class CSV:
    def __init__(self):
        self._data = []

    @property    
    def data(self):
        return self._data
    
    @data.setter
    def name(self, value):
        self._data = value