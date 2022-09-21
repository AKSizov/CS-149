# roses.py
# lab 3

#      @-->---->---
#       @----->->--
# @----->------->--
#   @->->----------
#            @->->-

# what a nice rose.

# in this lab, we take working code and make it ugly
# and less readable

def rose_drawing(rose):
    line1 = "-" * rose[0]
    line2 = "-" * rose[1]
    line3 = "-" * rose[2]
    full = "@%s>%s>%s" % (line1, line2, line3)
    return full


def padded_rose_drawing(rose, len):
    f_str = (" "*len) + rose_drawing(rose)
    return f_str


def rose_length(rose):
    return sum(rose) + 3


# sure, loops would be prettier. but they're still not allowed.
rose1 = (2, 4, 3)
rose2 = (5, 1, 2)
rose3 = (5, 7, 2)
rose4 = (1, 1, 10)
rose5 = (1, 1, 1)
lens = [rose_length(rose1),
        rose_length(rose2),
        rose_length(rose3),
        rose_length(rose4),
        rose_length(rose5)]
longest = max(lens)

print(padded_rose_drawing(rose1, longest - lens[0]))
print(padded_rose_drawing(rose2, longest - lens[1]))
print(padded_rose_drawing(rose3, longest - lens[2]))
print(padded_rose_drawing(rose4, longest - lens[3]))
print(padded_rose_drawing(rose5, longest - lens[4]))
