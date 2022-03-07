from enum import Enum


def find_participant(name: str, all: []):
    for item in all:
        if item.name.lower() == name.lower():
            return item
    return None


class weapon(Enum):
    punch = 2
    sword = 4
    spear = 6


class Human:
    """
    Classe qui définit un humain
    """

    def __init__(self, class_name: str, class_age: int, class_pv: int, class_weapon=weapon.punch):
        self.name = class_name
        self.age = class_age
        self.pv = class_pv
        self.alive = True
        self.weapon = class_weapon

    def attack(self, opponent):
        opponent.hurt(self.weapon.value)

    def hurt(self, damage: int):
        self.pv -= damage
        if self.pv <= 0:
            self.alive = False


participants = []
participants.append(Human("jason", 26, 15, weapon.sword))
participants.append(Human("bob", 22, 10, weapon.punch))

main_game = True
while main_game:
    choice = input("Voulez-vous attaquer? ")
    player = find_participant("jason", participants)
    enemy = find_participant("bob", participants)

    if choice == "oui":
        player.attack(enemy)
        enemy.attack(player)

        for participant in participants:
            print(f"{participant.name} a {participant.pv} points de vie")

            # name = input("Qui attaque?")
            # player1 = find_participant(name, participants)
            #
            # if player1:
            #     name = input("Qui est attaqué?")
            #     player2 = find_participant(name, participants)
            #     if player2:
            #         player1.attack(player2)
            #
