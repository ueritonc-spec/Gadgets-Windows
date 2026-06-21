class HistoryBuffer:
    def __init__(self, max_values=60):
        self.max_values = max_values
        self.values = []

    def add_value(self, value):
        self.values.append(value)

        if len(self.values) > self.max_values:
            self.values.pop(0)

    def get_values(self):
        return self.values