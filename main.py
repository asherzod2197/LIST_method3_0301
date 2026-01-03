class MyList:
    def __init__(self):
        self.data = []

    def extend(self, items):
        for item in items:
            self.data += [item]

    def show(self):
        print(self.data)

lst = MyList()

lst.extend([1, 2, 3])
lst.extend([4, 5])
lst.extend("ab")

lst.show()   
