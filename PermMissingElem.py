numbers = [2, 1, 3, 4]

def solution(A):
    #turning A into a set
    set_A = set(A)
    i = 1
    #checking if i is in the set, if so, add 1 to count and run the line again,
    #until the value i is not in the set, meaning it is the missing integer, and return it
    while i in set_A:
        i += 1
    return i

print(solution(numbers))