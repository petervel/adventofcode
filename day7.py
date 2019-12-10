import math
import itertools

dataInput = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]
testData = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
testData2= [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]

testB1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
testB2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

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

def opcode3(data, i, modes, inp=None):
    target = data[i + 1]
    if inp == None:
        inp = int(input("Input:"))
    #print("storing value " + str(inp) + " to location " + str(target))
    data[target] = inp
    return 2

def opcode4(data, i, modes, output=None):
    valA = getValue(data, i, modes, 1)
    if output == None:
        print(str(valA))
    else:
        output.append(valA)
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

class Amplifier:
    def __init__(self, data):
        self.data = data
        self.done = False
        self.step = 0

    def run(self, input):
        i = self.step
        inputIndex = 0
        output = []
        while i < len(self.data):
            opcode = self.data[i]

            # print(str(i) + ") " + str(opcode))
            # print(data)

            modes = math.floor(opcode / 100)
            opcode = opcode % 100
            if opcode == 99:
                self.done = True
                print(output)
                break
            elif opcode == 1:
                i += opcode1(self.data, i, modes)
            elif opcode == 2:
                i += opcode2(self.data, i, modes)
            elif opcode == 3:  # input
                i += opcode3(self.data, i, modes, input[inputIndex])
                inputIndex += 1
            elif opcode == 4:  # output
                i += opcode4(self.data, i, modes, output)
                self.step = i
                return output.pop()
            elif opcode == 5:
                i = opcode5(self.data, i, modes)
            elif opcode == 6:
                i = opcode6(self.data, i, modes)
            elif opcode == 7:
                i += opcode7(self.data, i, modes)
            elif opcode == 8:
                i += opcode8(self.data, i, modes)
            else:
                print("UNKNOWN OPCODE " + str(opcode) + " at position " + str(i))
                exit(1)

def bruteInstance(data, params):
    amps = []
    for i in range(5):
        amps.append(Amplifier(data.copy()))

    result = 0
    i = 0
    while True:
        amp = amps[i]
        result = amp.run([params[i], result])
        if amp.done:
            return result
        i =  (i + 1) % 5

def brute(data, values):
    best = 0
    for params in itertools.permutations(values):
        result = bruteInstance(data, params)
        print(result)
        if result != None and result > best:
            best = result
    print(best)

def main():
    #brute(dataInput, range(5))
    brute(testB1, range(5,10))


main()