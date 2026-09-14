class Hero:
    def __init__(self, name, health, attack_power, armor_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.armor_power = armor_power

    def attack(self):
        return self.attack_power

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

    
