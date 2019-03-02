urls = (
    '/', 'index'
)


number = None
varia = 20023

class index:

    def test(self):
        global varia
        self.varia = 23
        print("test " + str(self.varia))

    def test2(self):
        global varia
        self.varia = 24
        print("test2 " + str(self.varia))

    def test3(self):
        print("test3 " + str(varia))


if __name__ == '__main__':
    t = index()
    t.test()
    t.test2()
    t.test3()


