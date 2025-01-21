# Given list of strings which are logs and an integer representing maximum time, determine which user has activity time
# of less than or equal to the maximum time. Sort and return those list of users.
# [Do not remember if sorting was asked based on user number or their activity time]
#
# Input :
# logs : ["12 10 sign-in", "5 100 sign-out", "12 20 sign-out", "5 10 sign-in", "8 20 sign-in", "8 50 sign-out"]
# maximumTime : 30
#
# Output : [8, 12]
#
# Explanation -
# User 12 - logged in time period - (signout time - signin time) - 20 - 10 = 10 < 30
# User 5 - logged in time period - (signout time - signin time) - 100 - 10 = 90 > 30
# User 8 - logged in time period - (signout time - signin time) - 50 - 20 = 30 == 30

def minimum_user_log(logs, max_time):
    users = {}
    session_time = []
    for log in logs:
        log_data = log.split(' ')
        if log_data[0] in users:
            log_time = abs(users[log_data[0]] - int(log_data[1]))
            if log_time <= max_time:
                session_time.append(log_data[0])
        else:
            users[log_data[0]] = int(log_data[1])
    return session_time


if __name__ == "__main__":
    print(minimum_user_log(["12 10 sign-in", "5 100 sign-out", "12 20 sign-out", "5 10 sign-in", "8 20 sign-in",
                            "8 50 sign-out"], 30))
