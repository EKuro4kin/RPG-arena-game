from dataclasses import dataclass
from skills import Skill, FuryPunch, HardShot

concrete_skill = Skill()
fury_punch_skill = FuryPunch()
hard_shot_skill = HardShot()


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: concrete_skill.name


WarriorClass = UnitClass("Воин", 60, 30, 0.8, 0.9, 1.2, fury_punch_skill.name)

ThiefClass = UnitClass("Вор", 50, 25, 1.5, 1.2, 1.0, hard_shot_skill.name)

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}
