from enum import Enum
from tkinter import *
from PIL import ImageTk, Image


def find_participant(name: str, all: []):
    for item in all:
        if item.name.lower() == name.lower():
            return item
    return None


def information_pv(action: str):
    message = []
    for participant in participants:
        participant_pv = f"{participant.name} a {participant.pv} points de vie"
        message.append(participant_pv)
        print(f"{participant.name} a {participant.pv} points de vie")
    label_information.config(text="\n".join(message))


def background_enemy_image():
    global enemy, minotaur_img, cyclops_img
    if enemy.name == "minotaur":
        img_monstrer.config(image=minotaur_img)
        root.config(bg="red")
    if enemy.name == "cyclops":
        root.config(bg="blue")
        img_monstrer.config(image=cyclops_img)


def click_change_enemy():                                            # rewrite this def correctly
    global enemy                                                     # Doesn't work with real methode (enemy) and return
    if enemy.name == "minotaur":
        new_enemy = find_participant("cyclops", participants)
        enemy = new_enemy
    else:
        new_enemy = find_participant("minotaur", participants)
        enemy = new_enemy
    print("current enemy: ", enemy.name)
    label_information.config(text=enemy.name)
    background_enemy_image()


def update_gui(tk_root: Tk, count_button:Button, count:int):
    if count >= 0:
        count_button.config(text=str(count))
        root.after(1000, update_gui, tk_root, count_button, count - 1)
    else:
        count_button.config(text="Start!", state=NORMAL)


class weapon(Enum):
    punch = 2
    sword = 4
    spear = 6


class Human:
    """
    Classe qui définit un humain
    """

    def __init__(self, class_name: str, class_pv: int, class_weapon=weapon.punch):
        self.name = class_name
        self.pv = class_pv
        self.alive = True
        self.weapon = class_weapon

    def attack(self, enemy):  # opponent
        enemy.hurt(self.weapon.value)

    def defence(self):
        self.pv += 2        # make random
        enemy.pv += 2       # make random

    def hurt(self, damage: int):
        self.pv -= damage
        if self.pv <= 0:
            self.not_alive()

    def not_alive(self):
        self.alive = False
        print(self.name, "Mort")
        # participants.remove()                       # remove self from the list participants

# List of humans in the game
participants = []
participants.append(Human("ulisse", 15, weapon.sword))
participants.append(Human("minotaur", 10, weapon.punch))
participants.append(Human("cyclops", 10, weapon.spear))


player = find_participant("ulisse", participants)
enemy = find_participant("minotaur", participants)

root = Tk()
root.geometry("500x400")
root.config(bg="red")

minotaur_img = ImageTk.PhotoImage(Image.open("minotaur.jpg"))
cyclops_img = ImageTk.PhotoImage(Image.open("cyclops.jpg"))

img_monstrer = Label(root, image=minotaur_img)
img_monstrer.pack()
img_monstrer.place(x=120, y=130)

button_attack = Button(root, bg="grey", width=10, height=5, text="Attack",
                       command=lambda:
                       [player.attack(enemy), enemy.attack(player), information_pv("You choose attack !")])
button_attack.pack()
button_attack.place(x=400, y=300)

button_defence = Button(root, bg="grey", width=10, height=5, text="Defence",
                        command=lambda: [player.defence(), information_pv("You choose defence !")])
button_defence.pack()
button_defence.place(x=10, y=300)

button_change_enemy = Button(root, bg="grey", width=12, height=5, text="Change enemy",
                             command=lambda: click_change_enemy())
button_change_enemy.pack()
button_change_enemy.place(x=10, y=170)

label_information = Label(root, bg="grey", width=40, height=5, text="minautor")
label_information.pack()
label_information.place(x=100, y=10)

button_potion = Button(root, bg="white", width=10, height=5, state=DISABLED, text="",
                       command=lambda: [update_gui(root, button_potion, 4)])
button_potion.pack()
button_potion.place(x=400, y=170)

root.after(1000, update_gui, root, button_potion, 4)
root.mainloop()

# main_game = True
# while main_game:
#     choice = input("Voulez-vous attaquer? ")
#     player = find_participant("ulisse", participants)
#     enemy = find_participant("bob", participants)
#
#     if choice == "oui":
#         player.attack(enemy)
#         enemy.attack(player)
#
#         for participant in participants:
#             print(f"{participant.name} a {participant.pv} points de vie")
