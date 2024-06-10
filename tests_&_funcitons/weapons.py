dexterity_based_weapons = {
    "Ranged Weapons": {
        "shortbow": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d6",
            "Damage Type": "Pierce",
            "Minimum Stat": 10,
        },
        "longbow": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d8",
            "Damage Type": "Pierce",
            "Minimum Stat": 12,
        },
        "crossbowLight": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d8",
            "Damage Type": "Pierce",
            "Minimum Stat": 12,
        },
        "crossbowMedium": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d10",
            "Damage Type": "Pierce",
            "Minimum Stat": 14,
        },
        "crossbowHeavy": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d12",
            "Damage Type": "Pierce",
            "Minimum Stat": 14,
        },
    },
    "Melee Weapons": {
        "dagger": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d4",
            "Damage Type": "Pierce",
            "Minimum Stat": 10,
        },
        "whip": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d6",
            "Damage Type": "Slash",
            "Minimum Stat": 14,
        },
        "escrima": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d6",
            "Damage Type": "Blunt",
            "Minimum Stat": 14,
        },
        "scimitar": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d6",
            "Damage Type": "Slash",
            "Minimum Stat": 12,
        },
        "shortsword": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d6",
            "Damage Type": "Pierce",
            "Minimum Stat": 10,
        },
        "rapier": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d8",
            "Damage Type": "Pierce",
            "Minimum Stat": 14,
        },
        "quarterstaff": {
            "Damage Stat": "Dexterity",
            "Damage Dice": "d8",
            "Damage Type": "Blunt",
            "Minimum Stat": 14,
        },
    },
}


strength_based_weapons = {
    "hatchet": {
        "Damage Stat": "Strength",
        "Damage Dice": "d6",
        "Damage Type": "Slash",
        "Minimum Stat": 10,
    },
    "machete": {
        "Damage Stat": "Strength",
        "Damage Dice": "d6",
        "Damage Type": "Slash",
        "Minimum Stat": 10,
    },
    "mace": {
        "Damage Stat": "Strength",
        "Damage Dice": "d6",
        "Damage Type": "Blunt",
        "Minimum Stat": 10,
    },
    "pickaxe": {
        "Damage Stat": "Strength",
        "Damage Dice": "d6",
        "Damage Type": "Pierce",
        "Minimum Stat": 10,
    },
    "longsword": {
        "Damage Stat": "Strength",
        "Damage Dice": "d8",
        "Damage Type": "Slash",
        "Minimum Stat": 12,
    },
    "warhammer": {
        "Damage Stat": "Strength",
        "Damage Dice": "d8",
        "Damage Type": "Blunt",
        "Minimum Stat": 10,
    },
    "spear": {
        "Damage Stat": "Strength",
        "Damage Dice": "d8",
        "Damage Type": "Pierce",
        "Minimum Stat": 10,
    },
    "claymore": {
        "Damage Stat": "Strength",
        "Damage Dice": "d10",
        "Damage Type": "Slash",
        "Minimum Stat": 16,
    },
    "battleaxe": {
        "Damage Stat": "Strength",
        "Damage Dice": "d10",
        "Damage Type": "Slash",
        "Minimum Stat": 14,
    },
    "maul": {
        "Damage Stat": "Strength",
        "Damage Dice": "2d6",
        "Damage Type": "Blunt",
        "Minimum Stat": 16,
    },
    "horsechopper": {
        "Damage Stat": "Strength",
        "Damage Dice": "2d6",
        "Damage Type": "Slash",
        "Minimum Stat": 16,
    },
}

path = "/Users/Jake"

separator = "+"
path_tokens = path.split("/")
print(separator.join(path_tokens))
