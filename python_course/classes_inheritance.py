# наследование - для того, чтобы не повторяться, напишем общий класс Персонажи
class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self):
        print(f"{self.character_name} attacks with {self.attack_power} power")


    def __str__(self):
        return(f"{self.character_name} (level: {self.level}, hp: {self.health_points})")


# создали класс, теперь создаем классы-наследники

class Ork(Character):
    base_health_points = 100 # три атрибута класса Орк - здоровье, атака, имя персонажа
    base_attack_power = 10
    character_name = "Ork"

# создаем экземпляр класса Орк
ork_1 = Ork(level = 1)
ork_1.attack()
print(ork_1)

class Elf(Character):
    base_health_points = 50 # три атрибута класса Орк - здоровье, атака, имя персонажа
    base_attack_power = 15
    character_name = "Elf"

elf_1 = Elf(level = 2)
elf_1.attack()
print(elf_1)