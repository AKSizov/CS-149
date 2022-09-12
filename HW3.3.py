# scoring.py
# hw 3.3

# Enter the player's last name: Tucker

# Tucker scored 216 points.

stats = {
    "Jefferson": 388,
    "Hazell": 	 237,
    "Tucker": 	 216,
    "McDaniel":  195,
    "Green": 	 140
}

lastName = input("Enter the player's last name: ")
print()
print("%s scored %s points." % (lastName, stats[lastName]))
