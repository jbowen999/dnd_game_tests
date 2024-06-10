def main():
    grid = [0, 0]
    map_action(grid)


def move(direction, grid):
    if direction == 1:
        grid[1] += 1
        map_action(grid)
    elif direction == 2:
        grid[1] -= 1
        map_action(grid)
    elif direction == 3:
        grid[0] -= 1
        map_action(grid)
    elif direction == 4:
        grid[0] += 1
        map_action(grid)
    else:
        print("Invalid Option")
        map_action(grid)


def map_action(grid):
    try:
        direction = int(
            input(
                f"You are at ({grid[0]},{grid[1]})\nWhere do you want to go?\nNorth[1]\nSouth[2]\nEast[3]\nWest[4]\n"
            )
        )
    except ValueError:
        print("Invalid Option")
        map_action(grid)
    else:
        move(direction, grid)


# if __name__ == "__main__":
#     main()
