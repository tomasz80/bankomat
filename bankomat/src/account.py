class Account():
    def __init__(self):
        self.amount = 0;

    def add(self, value):
        self.amount = self.amount +  int(value)

    def sub(self, value):
        if self.amount >= value:
            self.amount = self.amount - value
            return True
        else:
            return False