def maltipy(mx, my):
    sum: int = 0
    for i in range(len(mx)):
        sum += mx[i] * my[i]
    return sum

def square(mx):
    sum: int = 0
    for i in range(len(mx)):
        sum += mx[i] * mx[i]
    return sum
