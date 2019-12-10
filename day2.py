data1 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,31,9,35,2,10,35,39,1,5,39,43,2,43,10,47,1,47,6,51,2,51,6,55,2,55,13,59,2,6,59,63,1,63,5,67,1,6,67,71,2,71,9,75,1,6,75,79,2,13,79,83,1,9,83,87,1,87,13,91,2,91,10,95,1,6,95,99,1,99,13,103,1,13,103,107,2,107,10,111,1,9,111,115,1,115,10,119,1,5,119,123,1,6,123,127,1,10,127,131,1,2,131,135,1,135,10,0,99,2,14,0,0]

data2 = [1,0,0,0,99]
data3 = [2,3,0,3,99]
data4 = [2,4,4,5,99,0]
data5 = [1,1,1,4,99,5,6,0,99]

def taskA(data):
    i = 0
    while i < len(data):
        opcode = data[i]
        if opcode == 99:
            break
        a = data[i+1]
        b = data[i+2]
        target = data[i+3]
        if opcode == 1:
            data[target] = data[a] + data[b]
        elif opcode == 2:
            data[target] = data[a] * data[b]
        i += 4

    print(data)

#taskA(data1)

def taskBhelper(data, op1, op2):
    data[1] = op1
    data[2] = op2
    i = 0
    while i < len(data):
        opcode = data[i]
        if opcode == 99:
            break
        a = data[i+1]
        b = data[i+2]
        target = data[i+3]
        if opcode == 1:
            data[target] = data[a] + data[b]
        elif opcode == 2:
            data[target] = data[a] * data[b]
        i += 4

    return data[0]

def taskB():
    for i in range(0,99):
        for j in range(0,99):
            if taskBhelper(data1.copy(), i, j) == 19690720:
                print(i)
                print(j)

taskB()