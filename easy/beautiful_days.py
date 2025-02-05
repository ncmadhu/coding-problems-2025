# Lily likes to play games with integers. She has created a new game where she determines the difference between a
# number and its reverse. For instance, given the number , its reverse is . Their difference is .
# The number  reversed is , and their difference is .
#
# She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a
# movie on a beautiful day.
#
# Given a range of numbered days,  and a number , determine the number of days in the range that are beautiful.
# Beautiful numbers are defined as numbers where  is evenly divisible by . If a day's value is a beautiful number,
# it is a beautiful day. Return the number of beautiful days in the range.
#
# Function Description
#
# Complete the beautifulDays function in the editor below.
#
# beautifulDays has the following parameter(s):
#
# int i: the starting day number
# int j: the ending day number
# int k: the divisor
# Returns
#
# int: the number of beautiful days in the range
def beautiful_days(i, j, k):
    b_days = 0
    for day in range(i, j+1):
        reverse = 0
        n = day
        while n:
            remainder =  n % 10
            reverse = reverse * 10 + remainder
            n = n // 10
        if abs(day - reverse) % k == 0:
            b_days += 1
    return b_days




if __name__ == "__main__":
    print(beautiful_days(20, 23, 6))
