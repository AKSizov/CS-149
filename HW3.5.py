# bar_chart.py
# hw 3.5

# ----------------------------------------
# Python   : =============================
# Java     : ===================
# JavaScri : ========
# C#       : =======
# PHP      : ======
# ----------------------------------------
# min: 6.20 max: 29.90
import math

labels = ['Python', 'Java', 'JavaScript', 'C#', 'PHP']
data = [29.9, 19.1, 8.2, 7.3, 6.2]
barChar = "="

print("-----------" + "-"*math.floor(max(data)))
# THE AUTOGRADER DOES NOT LIKE LOOPS!!!
# i = 0
# while i < len(labels):
#     print(f"{labels[i]:8.8s} : {barChar * (math.floor(data[i]))}")
#     i += 1
# THEREFORE THIS SOLUTION WILL FAIL!!!
print(f"{labels[0]:8.8s} : {barChar * (math.floor(data[0]))}")
print(f"{labels[1]:8.8s} : {barChar * (math.floor(data[1]))}")
print(f"{labels[2]:8.8s} : {barChar * (math.floor(data[2]))}")
print(f"{labels[3]:8.8s} : {barChar * (math.floor(data[3]))}")
print(f"{labels[4]:8.8s} : {barChar * (math.floor(data[4]))}")
print("-----------" + "-"*math.floor(max(data)))
print(f"min: {min(data):.2f} max: {max(data):.2f}")
