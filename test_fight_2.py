import rolls

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
    init_combat(player, enemy)


def init_combat(players, enemies):
    
