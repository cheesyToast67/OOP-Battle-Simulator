
import random 

class Hero:
    def __init__(self, name, armor_power):
        self.name = name
        self.health = random.randint(100,150)
        self.attack_power = random.randint(10,25)
        self.armor_power = armor_power

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        damage = damage - self.armor_power
        if damage < 0: damage = 0
        self.health -= damage
        if self.health < 0: self.health = 0
        print(f"{self.name} takes {damage} damage. Health: {self.health}")
        print(f"{self.name}'s armor stopped some of the damage.")

    def is_alive(self):
        if self.health == 0: return False
        else: return True

    
