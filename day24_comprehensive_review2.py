from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, List, Dict
from functools import reduce
import random

# ---------
# 1) 예외 & 유틸
# ---------

class StatError(ValueError):
    """잘못된 스탯이 들어오면 던지는 예외"""

def clamp(value: int, lo: int, hi: int) -> int:
    return max(lo, min(value, hi))


# ---------
# 2) 캐릭터 기본 클래스
# ---------
class Character:
    def __init__(self, name: str, hp: int, atk: int, defense: int):
        if hp <= 0 or atk < 0 or defense < 0:
            raise StatError(f"Invalid stats: hp={hp}, atk={atk}, def={defense}")
        self.name = name
        self._hp = hp
        self.atk = atk
        self.defense = defense
    
    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, value: int):
        self._hp = clamp(value, 0, 10**9)

    def is_alive(self) -> bool:
        return self.hp > 0
    
    def base_damage(self) -> int:
        spread = random.randint(-2, 2)
        return max(1, self.atk + spread)

    def take_damage(self, dmg: int) -> int:
        real = max(0, dmg - self.defense // 3)
        self.hp -= real
        return real
    
    def speak(self) -> str:
        return f"{self.name} 준비 완료 🐰"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, hp={self.hp}, atk={self.atk}, def={self.defense})"


# ---------
# 3) 플레이어 * 몬스터
# ---------
class Player(Character):
    def __init__(self, name: str, hp: int, atk: int, defense: int, crit_rate: float = 0.15):
        super().__init__(name, hp, atk, defense)
        self.crit_rate = crit_rate

    def speak(self) -> str:
        return f"{self.name} 🐰: 제가 가욧"

    def base_damage(self) -> int:
        dmg = super().base_damage()
        if random.random() < self.crit_rate:
            return int(dmg * 1.8)
        return dmg

class Monster(Character):
    def __init__(self, name: str, hp: int, atk: int, defense: int, frenzy: bool = False):
        super().__init__(name, hp, atk, defense)
        self.frenzy = frenzy

    def speak(self) -> str:
        mood = "흉폭" if self.frenzy else "차분"
        return f"{self.name} 🐇 {mood} 모드..."

    def base_damage(self) -> int:
        dmg = super().base_damage()
        return int(dmg * 1.3) if self.frenzy else dmg

# ---------
# 4) 스킬 시스템 (함수형 콜백)
# ---------
@dataclass
class Skill:
    name: str
    func: Callable[[Character, Character], Dict[str, int]]

    def cast(self, user: Character, target: Character) -> Dict[str, int]:
        return self.func(user, target)

# 몇 가지 스킬을 람다/클로저로 정의
def make_power_strike(mult: float = 1.5) -> Skill:
    def _impl(user: Character, target: Character):
        raw = int(user.base_damage() * mult)
        dealt = target.take_damage(raw)
        return {"damage": dealt, "raw": raw}
    return Skill("Power Strike", _impl)

bleed = Skill(
    "Bleed",
    lambda user, target: {"damage": target.take_damage(max(1, user.base_damage() - 2)), "raw": user.base_damage()}
)

guard_break = Skill(
    "Guard Break",
    lambda user, target: {"damage": target.take_damage(user.base_damage() + target.defense // 4), "raw": user.base_damage()}
)


# ---------
# 5) 아이템 (dataclass)
# ---------
@dataclass
class Item:
    name: str
    effect: Callable[[Character], str]

    def use(self, target: Character) -> str:
        return self.effect(target)

# 포션들
small_potion = Item(
    "Small Potion",
    lambda t: setattr(t, "hp", t.hp + 10) or f"{t.name} HP +10"
)
guard_tonic = Item(
    "Guard Tonic",
    lambda t: setattr(t, "defense", t.defense + 2) or f"{t.name} DEF +2"
)


# ---------
# 6) 전투 매니저
# ---------
class Battle:
    def __init__(self, p: Player, m: Monster, p_skills: List[Skill], m_skills: List[Skill]):
        self.player = p
        self.monster = m
        self.p_skills = p_skills
        self.m_skills = m_skills
        self.turn = 1
        self.log: List[str] = []

    @staticmethod
    def coin() -> bool:
        return random.random() < 0.5
    
    def log_line(self, text: str):
        self.log.append(text)
        print(text)
    
    def player_turn(self):
        if self.player.hp <= 20 and self.coin():
            msg = small_potion.use(self.player)
            self.log_line(f"[Turn {self.turn}] {msg}")
            return
        skill = random.choice(self.p_skills)
        result = skill.cast(self.player, self.monster)
        self.log_line(f"[Turn {self.turn}] {self.player.name} uses {skill.name} -> {result['damage']} dmg (raw {result['raw']})")

    def monster_turn(self):
        if self.coin() and random.random() < 0.25:
            msg = guard_tonic.use(self.monster)
            self.log_line(f"[Turn {self.turn}] {msg}")
            return
        skill = random.choice(self.m_skills)
        result = skill.cast(self.monster, self.player)
        self.log_line(f"[Turn {self.turn}] {self.monster.name} uses {skill.name} -> {result['damage']} dmg (raw {result['raw']})")

    def run(self, max_turns: int = 20) -> str:
        self.log_line(self.player.speak())
        self.log_line(self.monster.speak())
        while self.player.is_alive() and self.monster.is_alive() and self.turn <= max_turns:
            if self.coin():
                self.player_turn()
                if self.monster.is_alive():
                    self.monster_turn()
            else:
                self.monster_turn()
                if self.player.is_alive():
                    self.player_turn()
            
            self.log_line(f"    ▶ Status: {self.player.name} HP={self.player.hp} / {self.monster.name} HP={self.monster.hp}")
            self.turn += 1

        
        # 결과 요약
        if self.player.is_alive() and not self.monster.is_alive():
            outcome = f"✅  {self.player.name} wins!"
        elif self.monster.is_alive() and not self.player.is_alive():
            outcome = f"✖️  {self.player.name} is defeated..."
        else:
            outcome = "🧂 Draw (time limit)"
        
        # 통계: 총 피해량 추정 (로그 파싱 대신 간단 집계)
        # 데미지 숫자만 추출해 합산 (컴프리헨션 + map + reduce)
        damages = [
            int(s.split("->")[1].split("dmg")[0].strip())
            for s in self.log if "->" in s
        ]
        total_damage = reduce(lambda a, b: a + b, damages, 0)
        self.log_line(f"Total damage dealt this battle: {total_damage}")

        # 파일 저장
        try:
            with open("battle_log.txt", "w", encoding="utf-8") as f:
                f.write("=== Mini Battle Sim Log === \n")
                for line in self.log:
                    f.write(line + "\n")
                f.write("\nResult: " + outcome + "\n")
                f.write(f"TotalDamage={total_damage}\n")
            self.log_line("📝 battle_log.txt saved.")
        except Exception as e:
            self.log_line(f"⚠️ failed to save log: {e}")
        
        return outcome


# ---------
# 7) 실행 (샘플 시나리오)
# ---------
if __name__ == "__main__":
    random.seed() # 매번 다른 결과

    try:
        p = Player(name = "Bunny", hp = 60, atk = 14, defense = 4, crit_rate = 0.2)
        m = Monster(name = "Ogre", hp = 75, atk = 12, defense = 6, frenzy = random.random() < 0.4)
    except StatError as e:
        print("❌ 스탯 설정 에러: ", e)
        raise

    # 스킬 세팅
    p_skills = [make_power_strike(1.6), bleed, guard_break]
    m_skills = [guard_break, bleed, make_power_strike(1.3)]

    # 전투
    battle = Battle(p, m, p_skills, m_skills)
    result = battle.run(max_turns = 18)
    print(result)

