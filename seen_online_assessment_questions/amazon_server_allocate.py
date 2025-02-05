# There are num_servers numbered from 0 to num_servers - 1
# The initial number of requests assigned to each servers is 0
# In the ith second, a request comes from IP hash of request[i] and it must be assigned to  the server with
# minimum number of requests amongst the first  request[i] servers. For example, if request[i] = 4, the request must be
# assigned to the server with the minimum number of requests amongst the servers with id [0,1,2,3]. If there are
# multiple servers with the same number of requests, choose the one with the minimum id. When a request is assigned to a
# server, its number of requests increases by 1
#
# Given the num_servers and the array request, for each request find the id of the server it is assigned to
#
#
# Example
#
# num_servers = 5
# request = [3,2,3,2,4]
# output =  [0,1,2,0,3]
#
# 3 --- > To server 0 from possible servers [0,1,2]   --> [1, 0, 0, 0, 0]     ---> [0]
# 2 --- > To server 1 from possible servers [0,1]     --> [1, 1, 0, 0, 0]     ---> [0,1]
# 3 --- > To server 2 from possible servers [0,1,2]   --> [1, 1, 1, 0, 0]     ---> [0,1,2]
# 2 --- > To server 0 from possible servers [0,1]     --> [2, 1, 1, 0, 0]     ---> [0,1,2,0]
# 4 --- > To server 3 from possible servers [0,1,2,3] --> [2, 1, 1, 1, 0]     ---> [0,1,2,0,3]



def test_function(num_servers, requests):
    allotted_servers = [0] * num_servers
    request_counts = [0] * num_servers
    for i, max_servers in enumerate(requests):
        min_server = 0
        for j in range(0, max_servers):
            if request_counts[j] < request_counts[min_server]:
                min_server = j
        request_counts[min_server] += 1
        allotted_servers[i] = min_server
    return allotted_servers


if __name__ == "__main__":
    print(test_function(5, [3,2,3,2,4]))
