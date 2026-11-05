X = 10
Y = 85
D = 30

def solution(X, Y, D):
    #get the total distance between the start and end point
    distance = Y - X
    #this is to check if the frog can perfectly jump from start to end
    #if distance % D == 0, then the frog lands exactly on Y
    #if not, then it takes distance // D + 1 jumps, as the frog needs to jump the remaning distance
    if distance % D == 0:
        return distance // D
    elif distance % D != 0:
        return distance // D + 1

print(solution(X, Y, D))