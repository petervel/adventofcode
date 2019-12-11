import math




def checkViews(y, x, grid):
    minX = -x
    maxX = len(grid[0])
    xRange = [x]
    if minX != 0:
        xRange += range(x-1, (x + minX) - 1, -1)
    if maxX != x:
        xRange += range(x + 1, maxX)

    minY = -y
    maxY = len(grid)
    yRange = [y]
    if minY != 0:
        yRange += range(y - 1, (y + minY) - 1, -1)
    if maxY != y:
        yRange += range(y + 1, maxY)

    #print("(" + str(x) + "," + str(y) +") => " + str(xRange) + " , " + str(yRange))

    counter = 0

    for i in yRange:
        for j in xRange:
            if i == y and j == x:
                continue

            c = grid[i][j]
            if c == '#':
                counter += 1
                #print("Found one at " + str(i) + "," + str(j) + ", counter: " + str(counter))
                rad = math.atan2(i - y, j - x)
                for a in range(len(grid)):
                    for b in range(len(grid[0])):
                        rad2 = math.atan2(a - y, b - x)
                        if rad == rad2:
                            grid[a][b] = '.'
    return counter

def cloneGrid(grid):
    result = []
    for row in grid:
        result.append(row.copy())
    return result

def resolve(grid):
    results = cloneGrid(grid)

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '#':
                val = str(checkViews(y, x, cloneGrid(grid)))
                while len(val) < 4:
                    val = ' ' + val
                results[y][x] = val
    return results

def printGrid(grid):
    max = 0
    for row in grid:
        printLine = ""
        for c in row:
            if c == '.':
                printLine += "    "
            else:
                val = int(c)
                if val > max:
                    max = val
                printLine += str(c)
        print(printLine)
    print("Max: " + str(max))

def run(data):
    rows = data.split('\n')
    grid = []
    for row in rows:
        grid.append(list(row))
    result = resolve(grid)
    printGrid(result)

def main():
    run(realData)





realData = "##.#..#..###.####...######\n\
#..#####...###.###..#.###.\n\
..#.#####....####.#.#...##\n\
.##..#.#....##..##.#.#....\n\
#.####...#.###..#.##.#..#.\n\
..#..#.#######.####...#.##\n\
#...####.#...#.#####..#.#.\n\
.#..#.##.#....########..##\n\
......##.####.#.##....####\n\
.##.#....#####.####.#.####\n\
..#.#.#.#....#....##.#....\n\
....#######..#.##.#.##.###\n\
###.#######.#..#########..\n\
###.#.#..#....#..#.##..##.\n\
#####.#..#.#..###.#.##.###\n\
.#####.#####....#..###...#\n\
##.#.......###.##.#.##....\n\
...#.#.#.###.#.#..##..####\n\
#....#####.##.###...####.#\n\
#.##.#.######.##..#####.##\n\
#.###.##..##.##.#.###..###\n\
#.####..######...#...#####\n\
#..#..########.#.#...#..##\n\
.##..#.####....#..#..#....\n\
.###.##..#####...###.#.#.#\n\
.##..######...###..#####.#"

test1 = ".#..#\n\
.....\n\
#####\n\
....#\n\
...##"

test2 = "......#.#.\n\
#..#.#....\n\
..#######.\n\
.#.#.###..\n\
.#..#.....\n\
..#....#.#\n\
#..#....#.\n\
.##.#..###\n\
##...#..#.\n\
.#....####"

test3 = "#.#...#.#.\n\
.###....#.\n\
.#....#...\n\
##.#.#.#.#\n\
....#.#.#.\n\
.##..###.#\n\
..#...##..\n\
..##....##\n\
......#...\n\
.####.###."

test4 = ".#..#..###\n\
####.###.#\n\
....###.#.\n\
..###.##.#\n\
##.##.#.#.\n\
....###..#\n\
..#.#..#.#\n\
#..#.#.###\n\
.##...##.#\n\
.....#.#.."

test5 = ".#..##.###...#######\n\
##.############..##.\n\
.#.######.########.#\n\
.###.#######.####.#.\n\
#####.##.#.##.###.##\n\
..#####..#.#########\n\
####################\n\
#.####....###.#.#.##\n\
##.#################\n\
#####.##.###..####..\n\
..######..##.#######\n\
####.##.####...##..#\n\
.#####..#.######.###\n\
##...#.##########...\n\
#.##########.#######\n\
.####.#.###.###.#.##\n\
....##.##.###..#####\n\
.#.#.###########.###\n\
#.#.#.#####.####.###\n\
###.##.####.##.#..##"



main()