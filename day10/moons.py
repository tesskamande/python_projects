def jupyter_moons():
    moon = {"Io": 1821.6, "Europa":1560.8, "Ganymede": 2634.1, "Callisto":2410.3}
    surface= {"Io": 1.796, "Europa":1.314, "Ganymede": 1.428, "Callisto":1.234}
    orbital_periods = {"Io": 1.769, "Europa":3.551, "Ganymede": 7.154, "Callisto":16.689}

    moon_name = input("Enter the name of a Galilean moon of jupyter? ")

    jupyter(moon, surface, orbital_periods, moon_name)
def jupyter(m, s, o, name):
        print()
        print("the radius is: ", m[name])
        print("the surface gravity is: ", s[name])
        print("the orbital days is: ",o[name])

jupyter_moons()