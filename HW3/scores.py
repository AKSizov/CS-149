# scores.py
# hw 3.2

# must have score_list

# Total points: 35
# Average points: 7.0
# Number of 0 point games: 1
# Last game score: 15

score_list = [5, 5, 1, 0]

print("Total points: %s" % (sum(score_list)))
print(f"Average points: {(sum(score_list)/len(score_list)):.1f}")
print("Number of 0 point games: %s" % (score_list.count(0)))
print("Last game score: %s" % (score_list[-1]))
