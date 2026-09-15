
from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Gauntlet"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = hero.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} won the battle!")
    else:
        print(f"{enemy.name} won the battle!")


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    """Creates the first goblin and enters him into the arena"""
    goblin = Goblin("Remmy Crusher of Skulls and Emperor of Power")
    print(f"{goblin.name} enters the arena with {goblin.health} health.\n")

    """Creates the second goblin and enters him into the arena"""
    goblin2 = Goblin("Bob")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.\n")

    """Creates the hero and enters them into the arena"""
    hero = Hero("Robert", 7)
    print(f"{hero.name} enters the arena with {hero.health} health.\n")

    battle(hero, goblin)
    hero.dance()


if __name__ == "__main__":
    main()
