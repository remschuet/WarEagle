class Human:
    def __init__(self, nom: str, age: int, pv=15):
        self.nom = nom
        self.age = age
        self.pv = pv


if __name__ == '__main__':
    h = Human("rems", 12)
    print(h.name)
    print
    print 