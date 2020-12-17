

def afc_west():
    print("KC")
    print("DEN"),
    print("LV")
    print("LAC")

def afc_east():
    print("BUF")
    print("NE")
    print("MIA")
    print("NYJ")


# Change this variable's value to print the different division
division = "east"

if division == "east":
    afc_east()
elif division == "west":
    afc_west()
else:
    afc_east()
    afc_west()
