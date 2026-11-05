numbers = [3, 8, 9, 7, 6]
K = 3

def solution(A, K):
    #in case the list is empty, return the empty list
    if not A: 
        return A
    #add the last element to the front of the list
    #remove it from the end of the list
    #repeat this process K times
    for i in range(K):
        A.insert(0, A[len(A)-1])
        A.pop(len(A)-1)
    return A


print(solution(numbers, K))
