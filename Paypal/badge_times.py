"""
We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often.
We have an unordered list of names and entry times over a single day.
Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period.
Your function should return each of the employees who fit that criteria,
plus the times that they badged in during the one-hour period.
If there are multiple one-hour periods where this was true for an employee,
just return the earliest one for that employee.

badge_times = [
  ["Paul",      "1355"], ["Jennifer",  "1910"], ["Jose",    "835"],
  ["Jose",       "830"], ["Paul",      "1315"], ["Chloe",     "0"],
  ["Chloe",     "1910"], ["Jose",      "1615"], ["Jose",   "1640"],
  ["Paul",      "1405"], ["Jose",       "855"], ["Jose",    "930"],
  ["Jose",       "915"], ["Jose",       "730"], ["Jose",    "940"],
  ["Jennifer",  "1335"], ["Jennifer",   "730"], ["Jose",   "1630"],
  ["Jennifer",     "5"], ["Chloe",     "1909"], ["Zhang",     "1"],
  ["Zhang",       "10"], ["Zhang",      "109"], ["Zhang",   "110"],
  ["Amos",         "1"], ["Amos",         "2"], ["Amos",    "400"],
  ["Amos",       "500"], ["Amos",       "503"], ["Amos",    "504"],
  ["Amos",       "601"], ["Amos",       "602"], ["Paul",   "1416"],
];

Expected output (in any order)
   Paul: 1315 1355 1405
   Jose: 830 835 855 915 930
   Zhang: 10 109 110
   Amos: 500 503 504

n: length of the badge records array
"""
import collections


def badge_times(records):
    login_times = collections.defaultdict(list)
    result_set = collections.defaultdict(list)
    for record in records:
        name = record[0]
        login_time = record[1]
        login_record = login_times[name]
        if len(login_record) > 2:
            login_record.pop(0)
        login_record.append(int(login_time))
        sorted_record = sorted(login_record)
        if len(sorted_record) == 3:
            curr_time =  (sorted_record[-1]  // 100) * 60 + sorted_record[-1]  % 100
            oldest_time = (sorted_record[0] // 100) * 60 + sorted_record[0] % 100
            if curr_time - oldest_time <= 60:
                result_set[name].append(sorted_record)
        login_times[name] = sorted_record
    return result_set



if __name__ == "__main__":
    records = [
        ["Paul", "1355"], ["Jennifer", "1910"], ["Jose", "835"],
        ["Jose", "830"], ["Paul", "1315"], ["Chloe", "0"],
        ["Chloe", "1910"], ["Jose", "1615"], ["Jose", "1640"],
        ["Paul", "1405"], ["Jose", "855"], ["Jose", "930"],
        ["Jose", "915"], ["Jose", "730"], ["Jose", "940"],
        ["Jennifer", "1335"], ["Jennifer", "730"], ["Jose", "1630"],
        ["Jennifer", "5"], ["Chloe", "1909"], ["Zhang", "1"],
        ["Zhang", "10"], ["Zhang", "109"], ["Zhang", "110"],
        ["Amos", "1"], ["Amos", "2"], ["Amos", "400"],
        ["Amos", "500"], ["Amos", "503"], ["Amos", "504"],
        ["Amos", "601"], ["Amos", "602"], ["Paul", "1416"],
    ]
    print(badge_times(records))
