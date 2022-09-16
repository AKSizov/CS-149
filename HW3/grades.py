# grades.py
# hw 3.4

# score 1: 74
# score 2: 65
# score 3: 97
# score 4: 100

# The final score for the course is 90.33%. Dropped lowest score 65.
# The remaining scores are 97, 74, and 100.

scores = []
scores.append(int(input("score 1: ")))
scores.append(int(input("score 2: ")))
scores.append(int(input("score 3: ")))
scores.append(int(input("score 4: ")))
print()
lowestScore = min(scores)
scores.remove(lowestScore)
averageGrade = sum(scores)/len(scores)
print(f"The final score for the course is {averageGrade:.2f}%. ", end="")
print("Dropped lowest score %s." % lowestScore)
print("The remaining scores are %s, %s, and %s."
      % (scores[0], scores[1], scores[2]))
