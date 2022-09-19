# roses.py
# lab 2.1

#      @-->---->---
#       @----->->--
# @----->------->--
#   @->->----------
#            @->->-

# what a nice rose.

def draw_line(vals, maxlen):
    line1 = "-" * vals[0]
    line2 = "-" * vals[1]
    line3 = "-" * vals[2]
    full = "@%s>%s>%s" % (line1, line2, line3)
    print(full.rjust(maxlen))


# sure, loops would be prettier. but they're still not allowed.
rose1 = (2, 4, 3)
rose2 = (5, 1, 2)
rose3 = (5, 7, 2)
rose4 = (1, 1, 10)
rose5 = (1, 1, 1)
lens = [sum(rose1) + 3,
        sum(rose2) + 3,
        sum(rose3) + 3,
        sum(rose4) + 3,
        sum(rose5) + 3]
longest = max(lens)

draw_line(rose1, longest)
draw_line(rose2, longest)
draw_line(rose3, longest)
draw_line(rose4, longest)
draw_line(rose5, longest)
