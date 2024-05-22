from dnd_game_tests.test_characters import *
from test_enemies import *
import random


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


def roll_d_20():
    roll = random.randint(1, 20)
    print(roll)
    return roll


def roll_d_8():
    roll = random.randint(1, 8)
    print(roll)
    return roll


def calculate_hit(ac, str, roll, prof):
    attack = str + roll + prof
    if attack > ac:
        return True
    else:
        return False


def attack(attacker, defender):
    attacker_strength = attacker["stats"]["strength"]
    defender_a_c = defender["armor_class"]
    strength_mod = calc_modifier(attacker_strength)
    proficiency_mod = cal_proficiency(attacker["level"])
    attack_roll = roll_d_20()
    if calculate_hit(defender_a_c, strength_mod, attack_roll, proficiency_mod):
        return roll_d_8() + int(strength_mod)
    else:
        return "Miss"


print(f">> {attack(mat, goblin)}")
