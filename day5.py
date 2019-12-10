import math

dataInput = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,91,67,225,1102,67,36,225,1102,21,90,225,2,13,48,224,101,-819,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,62,9,225,1,139,22,224,101,-166,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,102,41,195,224,101,-2870,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1101,46,60,224,101,-106,224,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1001,191,32,224,101,-87,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,76,90,225,1101,15,58,225,1102,45,42,224,101,-1890,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,101,62,143,224,101,-77,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,55,54,225,1102,70,58,225,1002,17,80,224,101,-5360,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,344,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,359,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,389,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1108,677,677,224,1002,223,2,223,1005,224,419,101,1,223,223,1008,226,677,224,102,2,223,223,1006,224,434,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,449,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,509,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,569,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,584,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,614,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,659,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
sample = [3,0,4,0,99]
sample2 = [1002,4,3,4,33]

test1 = [3,9,8,9,10,9,4,9,99,-1,8]
test2 = [3,9,7,9,10,9,4,9,99,-1,8]
test3 = [3,3,1108,-1,8,3,4,3,99]
test4 = [3,3,1107,-1,8,3,4,3,99]
test5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
test6 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
test7 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

def getValue(data, index, modes, offset):
    for i in range(offset-1):
        modes = modes // 10
    mode = modes % 10

    if mode == 1:
        address = index + offset
    else:
        address = data[index + offset]

    val = data[address]
    #print(str(index) + ", " + str(offset) + ", " + str(index + offset))
    #print("val at " + str(address) + " = " + str(val))
    return val

def opcode1(data, i, modes):
    #print(i)
    valA = getValue(data, i, modes, 1)
    valB = getValue(data, i, modes, 2)
    target = data[i + 3]
    data[target] = valA + valB
    #print(str(i) + ") modes " + str(modes) + ", instruction " + str(data[i]) + " , valA: " + str(valA) + ", valB " + str(valB) + ", target: " + str(target))
    return 4

def opcode2(data, i, modes):
    valA = getValue(data, i, modes, 1)
    valB = getValue(data, i, modes, 2)
    target = data[i + 3]
    data[target] = valA * valB
    #print(str(i) + ") modes " + str(modes) + ", instruction " + str(data[i]) + " , valA: " + str(valA) + ", valB " + str(valB) + ", target: " + str(target))
    return 4

def opcode3(data, i, modes):
    target = data[i + 1]
    inp = int(input("Input:"))
    #print("storing value " + str(inp) + " to location " + str(target))
    data[target] = inp
    return 2

def opcode4(data, i, modes):
    valA = getValue(data, i, modes, 1)
    print(str(valA))
    return 2

def opcode5(data, i, modes):
    valA = getValue(data, i, modes, 1)
    valB = getValue(data, i, modes, 2)
    #print(str(i) + ") modes " + str(modes) + ", instruction " + str(data[i]) + " , valA: " + str(valA) + ", valB " + str(valB))
    if valA != 0:
        return valB
    return i + 3

def opcode6(data, i, modes):
    valA = getValue(data, i, modes, 1)
    valB = getValue(data, i, modes, 2)
    if valA == 0:
        return valB
    return i + 3

def opcode7(data, i, modes):
    valA = getValue(data, i, modes, 1)
    valB = getValue(data, i, modes, 2)
    target = data[i + 3]
    if valA < valB:
        data[target] = 1
    else:
        data[target] = 0
    return 4

def opcode8(data, i, modes):
    valA = getValue(data, i, modes, 1)
    valB = getValue(data, i, modes, 2)
    target = data[i + 3]
    if valA == valB:
        data[target] = 1
    else:
        data[target] = 0
    #print(str(i) + ") modes " + str(modes) + ", instruction " + str(data[i]) + " , valA: " + str(valA) + ", valB " + str(valB) + ", target: " + str(target))
    return 4

def taskA(data):
    i = 0
    while i < len(data):
        opcode = data[i]

        #print(str(i) + ") " + str(opcode))
        #print(data)

        modes = math.floor(opcode/100)
        opcode = opcode % 100
        if opcode == 99:
            break
        elif opcode == 1:
            i += opcode1(data, i, modes)
        elif opcode == 2:
            i += opcode2(data, i, modes)
        elif opcode == 3:
            i += opcode3(data, i, modes)
        elif opcode == 4:
            i += opcode4(data, i, modes)
        elif opcode == 5:
            i = opcode5(data, i, modes)
        elif opcode == 6:
            i = opcode6(data, i, modes)
        elif opcode == 7:
            i += opcode7(data, i, modes)
        elif opcode == 8:
            i += opcode8(data, i, modes)
        else:
            print("UNKNOWN OPCODE " + str(opcode) + " at position " + str(i))
            exit(1)

    return data[0]

def main():
    taskA(dataInput)
    #taskA(sample2)

main()