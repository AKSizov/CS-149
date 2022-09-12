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
i = 0
while i < len(labels):
    print(f"{labels[i]:8.8s} : {barChar * (math.floor(data[i]))}")
    i += 1
print("-----------" + "-"*math.floor(max(data)))
print(f"min: {min(data):.2f} max: {max(data):.2f}")
