def calc_stats(char_class):
    if char_class == "wizard":
        return {
            "strength": 8,
            "dexterity": 14,
            "constitution": 13,
            "intelligence": 15,
            "wisdom": 12,
            "charisma": 10,
        }
    elif char_class == "fighter":
        return {
            "strength": 15,
            "dexterity": 14,
            "constitution": 13,
            "intelligence": 8,
            "wisdom": 12,
            "charisma": 10,
        }
    elif char_class == "rogue":
        return {
            "strength": 8,
            "dexterity": 15,
            "constitution": 13,
            "intelligence": 12,
            "wisdom": 10,
            "charisma": 14,
        }
    else:
        return {
            "strength": 8,
            "dexterity": 14,
            "constitution": 13,
            "intelligence": 10,
            "wisdom": 12,
            "charisma": 15,
        }
