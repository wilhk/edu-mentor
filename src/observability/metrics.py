class Metrics:
    def __init__(self):
        self.counters = {}

    def increment(self, name: str, value: int = 1):
        self.counters[name] = self.counters.get(name, 0) + value

    def to_dict(self):
        return dict(self.counters)


metrics = Metrics()
