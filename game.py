from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Gauntlet"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Remmy Crusher of Skulls and Emperor of Power")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblin2 = Goblin("Bob")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")

    hero = Hero("Robert", 100, 20, 5)
    print(f"{hero.name} enters the arena with {hero.health} health.")

    hero_damage = hero.attack()
    goblin.take_damage(hero_damage)

    gob_damage = goblin.attack()
    hero.take_damage(gob_damage)



if __name__ == "__main__":
    main()
