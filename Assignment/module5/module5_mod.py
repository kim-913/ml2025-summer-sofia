class InputProcessor:
    def __init__(self):
        self.numbers = []

    def insert_number(self, num):
        self.numbers.append(num)

    def search_number(self, x):
        try:
            return self.numbers.index(x) + 1
        except ValueError:
            return -1
