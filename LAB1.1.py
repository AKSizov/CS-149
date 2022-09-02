# = Bike Race Average Speed Calculator =

# How many miles did you race? 18.66 
# How much time did that take you in hours, minutes, and seconds? 
#   Hours: 0 
#   Minutes: 43 
#   Seconds: 49 

# Your speed was 25.55 mph, which is 41.12 kph.

print("= Bike Race Average Speed Calculator =")
print()
x = float(input("How many miles did you race? "))
print("How much time did that take you in hours, minutes, and seconds?")
h = float(input("  Hours: "))
m = float(input("  Minutes: "))
s = float(input("  Seconds: "))
print()
tS = h*60*60 + m*60 + s
mph = x/(tS/3600)
print(f"Your speed was {mph:.2f} mph, which is {mph*1.60934:.2f} kph.")
