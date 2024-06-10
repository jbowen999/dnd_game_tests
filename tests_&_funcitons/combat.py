from test_characters import *
from test_enemies import *
import rolls


# COMBAT TEST ///////////////////////


def calc_modifier(stat):
    return (stat - 10) / 2


def cal_proficiency(level):
    if level >= 17:
        return 6
    elif 13 <= level <= 16:
        return 5
    elif 9 <= level <= 12:
        return 4
    elif 5 <= level <= 9:
        return 3
    else:
        return 2


def calculate_hit(ac, str, roll, prof):
    attack = str + roll + prof
    if attack > ac:
        return True
    else:
        return False


def attack(attacker, defender):
    attacker_stat = attacker["attack_stat"]
    mod_stat = attacker["stats"][attacker_stat]
    modifier = calc_modifier(mod_stat)
    proficiency_mod = cal_proficiency(attacker["level"])
    weapon = attacker["equipment"]["weapon"]
    print(weapon)
    defender_a_c = defender["armor_class"]
    attack_roll = rolls.roll_d_20()
    if calculate_hit(defender_a_c, modifier, attack_roll, proficiency_mod):
        damage_roll = rolls.roll_d_8()
        damage = damage_roll + int(modifier)
        print(f"Damage Roll: {damage_roll}")
        return f"You deal {damage} damage to {defender['name']}"
    else:
        return "Miss"


# print(f">> {attack(mat, goblin)}")


def use_item():
    return None


def initiative_roll(party, enemies):
    return None


def lose_hp(current_hp, damage):
    return None
