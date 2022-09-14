# happy.py
# hw 4.2

# If you're happy and you know it, clap your hands
# If you're happy and you know it, clap your hands
# If you're happy and you know it, and you really want to show it
# If you're happy and you know it, clap your hands

# If you're happy and you know it, slap your knees
# If you're happy and you know it, slap your knees
# If you're happy and you know it, and you really want to show it
# If you're happy and you know it, slap your knees

# If you're happy and you know it, turn around
# If you're happy and you know it, turn around
# If you're happy and you know it, and you really want to show it
# If you're happy and you know it, turn around

# If you're happy and you know it, pat your head
# If you're happy and you know it, pat your head
# If you're happy and you know it, and you really want to show it
# If you're happy and you know it, pat your head

# If you're happy and you know it, do all four
# If you're happy and you know it, do all four
# If you're happy and you know it, and you really want to show it
# If you're happy and you know it, do all four

pre = "If you're happy and you know it, "
line3 = pre + "and you really want to show it"


def pr(action):
    print(pre + action)
    print(pre + action)
    print(line3)
    print(pre + action)
    print()


pr("clap your hands")
pr("slap your knees")
pr("turn around")
pr("pat your head")
pr("do all four")
