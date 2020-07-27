# Uses python3
from sys import stdin, stdout


class KnapsackPack():
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight
    
    def __lt__(self, other):
        return self.cost < other.cost

def get_optimal_value(capacity, weights, values):
    value = 0
    left = capacity
    usedWeight = 0
    
    objsKnapsack = []

    for i in range(len(weights)):
        objsKnapsack.append(KnapsackPack(weights[i], values[i]))
    objsKnapsack.sort(reverse=True)

    i = 0
    stop = False

    while (stop != True):
        if (objsKnapsack[i].weight <= left):
            left -= objsKnapsack[i].weight
            usedWeight += objsKnapsack[i].weight
            value += objsKnapsack[i].value

            print("Pack ", i, " - Weight ", objsKnapsack[i].weight, " - Value ", objsKnapsack[i].value)
        else:
            print('entro aqui')
            available = capacity - usedWeight
            print('available {}'.format(available))
            value += objsKnapsack[i].value*(available/objsKnapsack[i].weight) 
            break
        
        if objsKnapsack[i].weight > left:
            i += 1
        print('i: {}, values: {}'.format(i, values))
        if i == len(values):
            stop = True
    
    return value


if __name__ == "__main__":
    
    n, capacity = map(int, input().split())
    values = []
    weights = []
    while (n):
        data = stdin.readline().strip().split()
        values.append(int(data[0]))
        weights.append(int(data[1]))
        n -= 1

    
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
