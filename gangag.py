print('Hello' + str(4))


class Data:
    id = 0

    def __init__(self, i):
        self.id = i

    def __str__(self):
        return 'Data[' + str(self.id) + ']'


print('Hello ' + str(Data(10)))
