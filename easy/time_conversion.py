# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# Example
#
# 12:01:00PM
# Return '12:01:00'.
#
# 12:01:00AM
# Return '00:01:00'.

def time_conversion(s):
    hour = s[0:2]
    min_sec = s[2:8]
    am_pm = s[8:]
    if hour == '12':
        if am_pm == 'AM':
            hour = '00'
    elif am_pm == 'PM':
        hour = int(hour) + 12
    return f'{hour:2}{min_sec}'


if __name__ == "__main__":
    print(time_conversion('12:01:00PM'))
    print(time_conversion('12:01:00AM'))
    print(time_conversion('01:01:00PM'))
    print(time_conversion('12:00:00AM'))
