A = [1, 3, 6, 4, 1, 2]

def solution(A):
    #turning A into a set
    A_set = set(A)
    #making the first i value 1, means that if if 1 is not in the set, 1 is returned
    i = 1
    #checking if i is in the set, if so, add 1 to count and run the line again,
    #until the value i is not in the set, meaning it is the missing integer, and return it
    while i in A_set:
        i += 1
    return i

print(solution(A))
