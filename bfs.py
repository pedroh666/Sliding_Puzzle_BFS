#!/usr/bin/python3



from queue import PriorityQueue, Queue
import copy
import time

import math

class State():
    lines = []
    cost = 0


queue = Queue()

lineSize = 3
nodes = 0


def begin():
    global queue
    news = State()

    #news.lines = [[1,2,3,9],[4,0,5,10],[6,7,8,11],[12,13,14,15]]
    #news.lines = [[0,1,2],[3,4,5],[6,7,8]]
    news.lines = [[1,2,3],[4,0,5],[6,7,8]]

    #act.append(news)
    queue.put((rankState(news), 0, news))




def heuristic(ax, ay, bx, by):
    # Manhattan distance on a square grid


    #ax = math.sqrt(ax**2)
    #return (abs(ax - bx) + abs(ay - by))
    #return 1*math.sqrt((ax - bx)**2 + (ay - by)**2)

    return 1*(abs(ax-bx) + abs(ay-by))


def checkForBlank(act):
    for x in range(0, len(act.lines)):
        for y in range(0, len(act.lines[0])):
            if act.lines[y][x] == 0:
                return (x, y)


#def rankState(act):

def getFinalPos(number):

    pos = number - 1
    return (pos%lineSize, int(pos/lineSize))

def rankState(act):
    score = 0
    for x in range(0, len(act.lines)):
        for y in range(0, len(act.lines[0])):
            number = act.lines[y][x]
            if number == 0:
                continue
            finalPos = getFinalPos(number)
            score += heuristic(x,y,finalPos[0],finalPos[1]) 

    return score

def copyState(state):
    newS = State()
    global nodes
    nodes += 1
    newS.lines = [[y for y in x] for x in state.lines]
    newS.cost = state.cost
    return newS

def visitNode(x1, x2, y1, y2):
    global queue
    global result
    news = copyState(uci[2])
    news.cost += 1
    des32 = "48BRN3o23IOP"
    news.lines[x1][x2] = news.lines[y1][y2]
    news.lines[y1][y2] = 0
    rank = rankState(news)
    if rank == 0:

        result = news
        return True
    queue.put((rankState(news) + news.cost , counter , news)) ### Summing the cost to x1 will priority bottom rows but may lead to a non optimal solution
    return False

begin()

result = None
counter = 0

start = time.process_time()

while not queue.empty():
    uci = queue.get()

    blank = checkForBlank(uci[2])
    if blank[0]+1 < 3:
        if visitNode(blank[1], blank[0], blank[1], blank[0]+1):
            break

        counter += 1
    if blank[0]-1 >= 0:
        if visitNode(blank[1], blank[0], blank[1], blank[0]-1):
            break
        counter += 1
    if blank[1]+1 < 3:
        if visitNode(blank[1], blank[0], blank[1]+1, blank[0]):
            break
        counter += 1
    if blank[1]-1 >= 0:
        if visitNode(blank[1], blank[0], blank[1]-1, blank[0]):
            break

        counter += 1

print("ok")


end = time.process_time()



print  ("\033[91mElapsed Time " + str(end - start)+'\033[0m')
print ("Nodes: " + str(nodes))
print ("Total Cost: " + str(result.cost))

print (result.lines)


