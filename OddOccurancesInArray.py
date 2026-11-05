numbers = [1, 2, 1, 2, 3]

def solution(A):
    #since only 1 value is being returned, unpaired will be an integer
    #starting at 0, as XOR has a useful property with 0 where x XOR 0 = x
    unpaired = 0
    #for each number in A, the XOR operation is applied to unpaired
    #a number XOR with itself is zero, meaning that all paired numbers cancel
    #leaving only the unpaired number, which is returned
    for number in A:
        unpaired ^= number
    return unpaired

print(solution(numbers))