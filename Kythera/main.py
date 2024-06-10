import character_creation as c_c, map_logic, calculations as calc


def main():
    grid = [0, 0]
    check = 0
    player = create_character()


def create_character():
    player_name = input("Welcome to Kythera... Who are you?\nEnter your name:")
    player_class = input(
        f"Choose your class:\nFighter[1] - {calc.classes_dict['fighter']['description']}\nWizard[2] - {calc.classes_dict['wizard']['description']}\nRogue[3] - {calc.classes_dict['rogue']['description']}\nBard[4] - {calc.classes_dict['bard']['description']}\n"
    )
    return c_c.Character(player_name, player_class)


if __name__ == "__main__":
    main()
