class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, "/ Points de vie: ", health, "/ Attaque: ", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def damage(self, damage):
        self.health -= damage

    def attack_player(self,target_player):
        target_player.damage(self.attack)


class Warrior(Player):

    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo,health,attack)
        self.armor = 3
        print("Bienvenue au guerrier", pseudo, "/ Points de vie: ", health, "/ Attaque: ", attack)

    def damage(self, damage):
        if self.armor > 0:
            self.armor -= 1
            damage = 0
        super().damage(damage)

    def blade(self):
        self.armor = 3
        print("Les points d'armure ont été rechargés.")

    def get_armor_points(self):
        return self.armor

player = Player("RoiPouss", 20, 2)
player.damage(3)

warrior = Warrior("Chamatou", 40, 3)
warrior.damage(5)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_points())

warrior.damage(5)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_points())

warrior.damage(5)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_points())

warrior.damage(5)
print("vie:", warrior.get_health(), "armure:", warrior.get_armor_points())

if issubclass(Warrior, Player):
    print("La classe Warrior est bien nenfant de la classe PLayer")