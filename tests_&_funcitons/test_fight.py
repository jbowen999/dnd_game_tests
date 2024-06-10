import test_characters, test_enemies, rolls

enemy = {
    "name": "Goblin",
    "description": "This goblin is UGLY",
    "hit_points": 20,
    "level": 2,
    "weapon": "scimitar",
    "armor_class": 13,
    "attack_stat": "dexterity",
    "stats": {
        "strength": 13,
        "dexterity": 17,
        "constitution": 13,
        "intelligence": 12,
        "wisdom": 13,
        "charisma": 14,
    },
}


player = {
    "name": "Julian",
    "class": "Warlord",
    "hit_points": 30,
    "level": 5,
    "weapon": "scimitar",
    "armor_class": 16,
    "attack_stat": "dexterity",
    "stats": {
        "strength": 13,
        "dexterity": 18,
        "constitution": 16,
        "intelligence": 14,
        "wisdom": 13,
        "charisma": 14,
    },
}


def main():
    print()
    print(
        "The goblin snarls with bloodstained teeth as it draws near.\nYou ready your weapon"
    )
    action(render_controls())


def render_controls():
    try:
        print('@--------------------------------@')
        
        selection = int(
            
            input("What will you do?\nExamine[1]\nAttack[2]\nItem[3]\nRun away[4]\n>>>>>>>")
        )
        
    except ValueError:
        print("Invalid\n")
        action(render_controls())

    else:
        if 1 <= selection <= 4:
            return selection
        else:
            print("Invalid\n")
            action(render_controls())


def action(selection):
    if selection == 1:
        print(f'{enemy['description']}, HP = {enemy["hit_points"]}')
        action(render_controls())
    elif selection == 2:
        attack(player, enemy, True)
    elif selection == 3:
        display_inventory()
    else:
        try_to_flee()


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


def attack(attacker, defender, you):
    attacker_stat = attacker["attack_stat"]
    mod_stat = attacker["stats"][attacker_stat]
    modifier = calc_modifier(mod_stat)
    proficiency_mod = cal_proficiency(attacker["level"])
    defender_a_c = defender["armor_class"]
    attack_roll = rolls.roll_d_20()
    if calculate_hit(defender_a_c, modifier, attack_roll, proficiency_mod):
        damage_roll = rolls.roll_d_8()
        damage = damage_roll + int(modifier)
        def_hp = decrease_hp(defender, damage) 
        if def_hp <= 0:
            print(f"{attacker['name']} deals {damage} damage to {defender['name']}")
            return f"{defender['name']} has died."
        else:
            print(f"{attacker['name']} deals {damage} damage to {defender['name']}")
            end_turn(you)
    else:
        print(f'{attacker["name"]} misses!')
        end_turn(you)


def display_inventory():
    print("You have no consumables")
    action(render_controls())


def try_to_flee():
    print("fail")
    end_turn(True)
    
    
def end_turn(your_turn):
    if your_turn == True:
        enemy_turn()
    else:
        action(render_controls())
        

def enemy_turn():
    print('@--------------------------------@')
    print(f'The {enemy["name"]} attacks!')
    attack(enemy, player, False)
    end_turn(False)


def decrease_hp(creature, damage):
    hp = creature['hit_points'] 
    hp -= damage
    return hp
    

if __name__ == "__main__":
    main()
