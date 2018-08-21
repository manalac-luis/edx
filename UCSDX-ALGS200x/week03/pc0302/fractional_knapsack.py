# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    bagcapacity = capacity
    value = 0.
    valperpound = [];
    # write your code here
    for i in range(0,len(weights)):
        valperpound.append(0.0);

    for i in range(0,len(weights)):
        valperpound[i]=values[i]/weights[i]
        #print("V ",values[i],"W ",weights[i],"VpP ",valperpound[i])

    while bagcapacity>0 :
        #print("capacity ",bagcapacity)
        index = -1
        highest = 0.
        for i in range(0,len(weights)):
            if (highest<valperpound[i] and weights[i]>0):
                highest = valperpound[i]
                index = i
        if (index>=0):
            #print("V ",values[index],"W ",weights[index],"VpP ",valperpound[index])
            if (bagcapacity>=weights[index]):
                bagcapacity=bagcapacity - weights[index]
                value = value + weights[index]*valperpound[index]
                weights[index]=0
            else:
                value = value + valperpound[index]*bagcapacity
                weights[index]=weights[index]-bagcapacity
                bagcapacity = 0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #print(data)
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    #print("capacity ",capacity)
    #print("weights ",weights)
    #print("values ",values)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
