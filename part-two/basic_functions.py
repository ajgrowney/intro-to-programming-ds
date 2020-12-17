def afc_east():
    print("BUF")
    print("NE")
    print("MIA")
    print("NYJ")

# TODO: Add an AFC North Function that prints all the teams

# TODO: Add an AFC South Function that prints all the teams

def afc_west():
    print("KC")
    print("DEN"),
    print("LV")
    print("LAC")


if __name__ == "__main__":
    # Change this variable's value to print the different division
    division = "east"

    if division == "east":
        afc_east()
    elif division == "west":
        afc_west()
    # TODO: Uncomment the lines below when you implement the functions above
    # elif division == "north":
    #     afc_north()
    # elif division == "south":
    #     afc_south()
    else:
        afc_east()
        afc_west()
        # afc_north()
        # afc_south()
