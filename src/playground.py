class Test:
    def __init__(self):
        self.value = 512
        self.check()

    def check(self):
        if self.value == 512:
            return True

address = Test()
print(address.check())
