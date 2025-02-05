# This is a staircase of size : 4
#
#    #
#   ##
#  ###
# ####

def print_staircase(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '#' * i)


if __name__ == "__main__":
    print_staircase(8)
