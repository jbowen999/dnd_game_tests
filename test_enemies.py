skeleton = {
    "name": "Skeleton",
    "race": "Undead",
    "class": "None",
    "level": 1,
    "alignment": "Lawful Evil",
    "hit_points": 13,
    "armor_class": 13,
    "speed": 30,
    "proficiencies": [],
    "languages": ["Understands all languages it knew in life but can't speak"],
    "equipment": {"weapons": ["Shortsword", "Shortbow"], "armor": ["None"]},
    "stats": {
        "strength": 10,
        "dexterity": 14,
        "constitution": 15,
        "intelligence": 6,
        "wisdom": 8,
        "charisma": 5,
    },
    "abilities": {
        "damage_vulnerabilities": "Bludgeoning",
        "damage_resistances": "Piercing, slashing from nonmagical attacks",
        "condition_immunities": "Poisoned",
        "undead_nature": "A skeleton doesn’t require air, food, drink, or sleep.",
    },
}

orc = {
    "name": "Orc",
    "race": "Orc",
    "class": "None",
    "level": 2,
    "alignment": "Chaotic Evil",
    "hit_points": 15,
    "armor_class": 13,
    "speed": 30,
    "proficiencies": ["Intimidation"],
    "languages": ["Common", "Orc"],
    "equipment": {"weapons": ["Greataxe", "Javelin"], "armor": ["Hide Armor"]},
    "stats": {
        "strength": 16,
        "dexterity": 12,
        "constitution": 16,
        "intelligence": 7,
        "wisdom": 11,
        "charisma": 10,
    },
    "abilities": {
        "aggressive": "As a bonus action, the orc can move up to its speed toward a hostile creature that it can see."
    },
}

goblin = {
    "name": "Goblin",
    "race": "Goblinoid",
    "class": "None",
    "level": 1,
    "alignment": "Neutral Evil",
    "hit_points": 7,
    "armor_class": 15,
    "speed": 30,
    "proficiencies": ["Stealth", "Survival"],
    "languages": ["Common", "Goblin"],
    "equipment": {"weapons": ["Scimitar", "Shortbow"], "armor": ["Leather Armor"]},
    "stats": {
        "strength": 8,
        "dexterity": 14,
        "constitution": 10,
        "intelligence": 10,
        "wisdom": 8,
        "charisma": 8,
    },
    "abilities": {
        "nimble_escape": "The goblin can take the Disengage or Hide action as a bonus action on each of its turns."
    },
}


balor = {
    "name": "Balor",
    "race": "Fiend (Demon)",
    "class": "None",
    "level": 20,
    "alignment": "Chaotic Evil",
    "hit_points": 262,
    "armor_class": 19,
    "speed": 40,
    "flying_speed": 80,
    "proficiencies": ["Intimidation", "Perception"],
    "languages": ["Abyssal", "Infernal", "Telepathy 120 ft."],
    "equipment": {"weapons": ["Longsword", "Whip"], "armor": ["Natural Armor"]},
    "stats": {
        "strength": 26,
        "dexterity": 15,
        "constitution": 22,
        "intelligence": 20,
        "wisdom": 16,
        "charisma": 22,
    },
    "abilities": {
        "fire_aura": "At the start of each of the balor's turns, each creature within 5 feet of it takes 10 fire damage, and flammable objects in the aura that aren't being worn or carried ignite.",
        "magic_resistance": "The balor has advantage on saving throws against spells and other magical effects.",
        "magic_weapons": "The balor's weapon attacks are magical.",
        "multiattack": "The balor makes two attacks: one with its longsword and one with its whip.",
        "death_throes": "When the balor dies, it explodes, and each creature within 30 feet of it must make a DC 20 Dexterity saving throw, taking 70 (20d6) fire damage on a failed save, or half as much damage on a successful one.",
    },
}

troll = {
    "name": "Troll",
    "race": "Giant",
    "class": "None",
    "level": 6,
    "alignment": "Chaotic Evil",
    "hit_points": 84,
    "armor_class": 15,
    "speed": 30,
    "proficiencies": ["Perception"],
    "languages": ["Giant"],
    "equipment": {"weapons": ["Claws", "Bite"], "armor": ["Natural Armor"]},
    "stats": {
        "strength": 18,
        "dexterity": 13,
        "constitution": 20,
        "intelligence": 7,
        "wisdom": 9,
        "charisma": 7,
    },
    "abilities": {
        "regeneration": "The troll regains 10 hit points at the start of its turn. If the troll takes acid or fire damage, this trait doesn't function at the start of the troll's next turn.",
        "keen_smell": "The troll has advantage on Wisdom (Perception) checks that rely on smell.",
        "multiattack": "The troll makes three attacks: one with its bite and two with its claws.",
    },
}
