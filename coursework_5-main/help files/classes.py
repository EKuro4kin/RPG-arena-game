from dataclasses import dataclass
from skills import Skill, FuryPunch, HardShot


# class ConcreteSkill:
#     def __init__(self, skill):
#         self.skill = skill


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: ConcreteSkill


fury_punch_skill = FuryPunch()
hard_shot_skill = HardShot()

WarriorClass = UnitClass("Воин", 60, 30, 0.8, 0.9, 1.2, fury_punch_skill)  # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов

ThiefClass = UnitClass("Вор", 50, 25, 1.5, 1.2, 1.0, hard_shot_skill)  # TODO действуем так же как и с войном

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
