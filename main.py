def find_participant(name: str, all:[]):
    for item in all:
        if item.nom.lower() == name.lower():
            return item
    return None


class Human:
    """
    Classe qui définit un humain
    """

    def __init__(self, class_nom: str, class_age: int, class_pv=15):
        self.nom = class_nom
        self.age = class_age
        self.pv = class_pv
        self.alive = True

    def attack(self, opponent):
        opponent.hurt()

    def hurt(self):
        self.pv -= 5
        if self.pv <= 0:
            self.alive = False

participants = []
participants.append(Human("jason", 26, 15))
participants.append(Human("bob", 22, 15))

main_game = True
while main_game:
    name = input("Qui attaque?")
    player1 = find_participant(name, participants)

    if player1:
        name = input("Qui est attaqué?")
        player2 = find_participant(name, participants)
        if player2:
            player1.attack(player2)

    for participant in participants:
        print(f"{participant.nom} a {participant.pv} points de vie")
