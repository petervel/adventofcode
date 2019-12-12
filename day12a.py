import math


class Moon:
    def __init__(self, coords):
        self.pos = coords
        self.vel = [0] * 3

    def updateSpeed(self, other):
        for i in range(3):
            if self.pos[i] < other.pos[i]:
                self.vel[i] += 1
            elif self.pos[i] > other.pos[i]:
                self.vel[i] -= 1

    def updatePosition(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    def print(self):
        print("pos=<x=" + str(self.pos[0]) + ", y=  " + str(self.pos[1]) + ", z= " + str(self.pos[2]) + ">, vel=<x=" + str(self.vel[0]) + ", y=  " + str(self.vel[1]) + ", z= " + str(self.vel[2]) + ">")

    def getPotential(self):
        sum = 0
        for i in range(3):
            sum += abs(self.pos[i])
        return sum

    def getKinetic(self):
        sum = 0
        for i in range(3):
            sum += abs(self.vel[i])
        return sum

    def getTotalEnergy(self):
        return self.getPotential() * self.getKinetic()

def tick(moons):
    for i, moon in enumerate(moons):
        for j, moon2 in enumerate(moons):
            if i == j:
                continue
            moon.updateSpeed(moon2)

    for moon in moons:
        moon.updatePosition()

def main():
    dataSource = data
    steps = 1000

    moons = []
    for d in dataSource:
        moons.append(Moon(d))

    step = 0
    while True:
        print("\nAfter " + str(step) + " steps:")
        for moon in moons:
            moon.print()

        if step >= steps:
            break

        tick(moons)
        step += 1

    totalEnergy = 0
    for moon in moons:
        totalEnergy += moon.getTotalEnergy()
    print("Total energy " + str(totalEnergy))

data = [
    [6, 10, 10],
    [-9, 3, 17],
    [9, -4, 14],
    [4, 14, 4],
]

test1 = [
    [-1, 0, 2],
    [2, -10, -7],
    [4, -8, 8],
    [3, 5, -1],
]

test2 = [
    [-8,-10,0],
    [5,5,10],
    [2,-7,3],
    [9,-8,-3],
]

main()