NUM_SIZE = 6

def check1(number):
    numStr = str(number)
    for i in range(NUM_SIZE-1):
        if numStr[i] == numStr[i+1]:
            return True
    return False

def check2(number):
    numStr = str(number)
    for i in range(NUM_SIZE-1):
        if int(numStr[i]) > int(numStr[i+1]):
            return False
    return True

def check3(number):
    numStr = str(number)
    lastIndex = None
    counter = 0
    for i in range(NUM_SIZE):
        a = numStr[i]
        if lastIndex == None:
            counter = 1
            lastIndex = a
        elif a == lastIndex:
            counter += 1
        else:
            if counter == 2:
                return True
            lastIndex = a
            counter = 1
    return counter == 2

def taskA(start, end):
    total = 0
    for i in range(start, end):
        if check1(i) and check2(i) and check3(i):
            print(i)
            total += 1
    return total

def main():
    solutions = taskA(246515, 739105)

    print(solutions)

main()
