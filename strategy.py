
class Strategy():
    def __init__(self, asset_a, asset_b):
        self.asset_a = asset_a
        self.asset_b = asset_b

    @property
    def asset_a(self):
        return self._asset_a

    @asset_a.setter
    def asset_a(self, value):
        self._asset_a = value

    @property
    def asset_b(self):
        return self._asset_b

    @asset_b.setter
    def asset_b(self, value):
        self._asset_b = value

    def get_next_action(self):
        pass

    def valid_pair(self):
        pass