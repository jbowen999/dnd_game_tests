def calc_stats(char_class):
    if char_class == 1:
        return classes_dict["fighter"]["stats"]
    elif char_class == 2:
        return classes_dict["wizard"]["stats"]
    elif char_class == 3:
        return classes_dict["rogue"]["stats"]
    else:
        return classes_dict["bard"]["stats"]


classes_dict = {
    "fighter": {
        "stats": {
            "strength": 15,
            "dexterity": 14,
            "constitution": 13,
            "intelligence": 8,
            "wisdom": 12,
            "charisma": 10,
        },
        "description": "This is the description of the FIGHTER class",
    },
    "wizard": {
        "stats": {
            "strength": 8,
            "dexterity": 14,
            "constitution": 13,
            "intelligence": 15,
            "wisdom": 12,
            "charisma": 10,
        },
        "description": "This is the description of the WIZARD class",
    },
    "rogue": {
        "stats": {
            "strength": 8,
            "dexterity": 15,
            "constitution": 13,
            "intelligence": 12,
            "wisdom": 10,
            "charisma": 14,
        },
        "description": "This is the description of the ROGUE class",
    },
    "bard": {
        "stats": {
            "strength": 8,
            "dexterity": 14,
            "constitution": 13,
            "intelligence": 10,
            "wisdom": 12,
            "charisma": 15,
        },
        "description": "This is the description of the BARD class",
    },
}
