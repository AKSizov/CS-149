# feet_conversion.py
# lab 1.2

# 1 mile is 5280 feet and 1 furlong is 660 feet

# Enter a total number of feet: 12345

# 12345 total feet is 2 mile(s), 2 furlong(s), and 465 feet.

x = int(input("Enter a total number of feet: "))
print()
m = x//5280
f = (x-(m*5280))//660
fe = x-((m*5280)+(f*660))
print("%s total feet is %s mile(s), %s furlong(s), and %s feet."
      % (x, m, f, fe))
