class Human:
    def __init__(self, nom: str, age: int, pv=15) -> None:
        self.nom = nom
        self.age = age
        self.pv = pv


    def mourrir(self):
        self.pv = 0

if __name__ == '__main__':
    h = Human("rems", 12)
    print(h.name)    
    print()
