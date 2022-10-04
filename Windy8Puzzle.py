#Ryan Schanerberger & Alexis Tucker
#CIS 479
#Windy 8-Puzzle
from array import*
from heapq import*
from mimetypes import init

class pq:
   def __init__(self, minHeap = None):
       if minHeap is None:
          self.minHeap = []
   #return top priority item
   def peek(self):
      return self.minHeap[0]
   #insert an item into the heap
   def insert(self, item):
      heappush(self.minHeap, item)
   #pops the top item of the heap 
   def remove(self):
      popped = heappop(self.minHeap)
      heapify(self.minHeap)
      return popped
   #need to full print heap
   def printHeap(self):
      for i in self.minHeap:
         print(i, end = ' ')

class aGraph:
   def __init__(self,gDict=None):
      if gDict is None:
         gDict = {}
      self.gDict = gDict
   def getVertices(self):
      return list(self.gDict.keys())
   def getEdges(self):
      return self.findEdges()
#Add vertex
   def addVertex(self, v):
      if v not in self.gDict:
         self.gDict[v] = []
#Add an edge
   def addEdge(self, edge):
      edge = set(edge)
      (v1, v2) = tuple(edge)
      if v1 in self.gDict:
         self.gDict[v1].append(v2)
      else:
         self.gDict[v1] = [v2]
#List the edges of graph
   def findEdges(self):
      edgename = []
      for vx in self.gDict:
         for nxtvx in self.gDict[vx]:
            if {nxtvx, vx} not in edgename:
               edgename.append({vx, nxtvx})
      return edgename

#initial state
initArr = [2, 8, 3, 6, 7, 4, 1, 5, 0]
#2, 8, 3
#6, 7, 4
#1, 5, 0
#goal state
goalArr = [1, 2, 3, 8, 0, 4, 7, 6, 5]
#1, 2, 3
#8, 0, 4
#7, 6, 5

#=================================================================#
#note for the array: up == -3, down == +3, left == -1, right == +1#
#=================================================================#
# Create the dictionary with graph elements
initialSt = { 
   "2" : ["8","6"],
   "8" : ["2", "3", "7"],
   "3" : ["8", "4"],
   "6" : ["7", "1"],
   "7" : ["6", "8", "4", "5"],
   "4" : ["7", "3", "0"] ,
   "1" : ["6", "5"],
   "5" : ["1", "7", "0"],
   "0" : ["5", "4"]
}

myTup = (1, 2, 3, 4)

test = 'T2'

num = 1000

def hashToTable(table, member):
   hashVal = hash(str(member))
   table[str(member)] = [hashVal]

#=================================================================#
#note for the hVal: up == 1, down == 3, left == 2, right == 2#
#=================================================================#
#=================================================================#
#note for the array: up == -3, down == +3, left == -1, right == +1#
#=================================================================#

def aHeuristic(current, goal):
   i = 0
   hVal = 0
   for i in range(1,9):
      print("Finding", i, ":")
      t1 = goal.index(i)
      t2 = current.index(i)
      found = t1 - t2
      print(found)
      #if found is greater than 0, we have to go up or left
      if(found > 0):
         while found > 3:
            found = found - 3
            hVal = hVal + 1
         while found > 0:
            found = found - 1
            hVal = hVal + 2
      if(found < 0):
         while found <= -3:
            found = found + 3
            hVal = hVal + 3
            
         while found < 0:
            found = found + 1
            hVal = hVal + 2
      return hVal


def goal(num, current, goal):
   gVal = 0
   t1 = goal.index(num)
   t2 = current.index(num)
   found = t1 - t2
   if(found > 0):
      while found > 3:
         found = found - 3
         gVal = gVal + 1
      while found > 0:
         found = found - 1
         gVal = gVal + 2
   if(found < 0):
      while found <= -3:
         found = found + 3
         gVal = gVal + 3
            
      while found < 0:
         found = found + 1
         gVal = gVal + 2
   return gVal

def testMove(move, current):
   newCurr = current
   zero = newCurr.index(0)
   swapNum = newCurr[move]
   newCurr[zero] = swapNum
   newCurr[move] = 0
   print(newCurr)
   return newCurr

def checkPossibleMoves(node):
   i = node.index(0)
   validMoves = {'R':(i+1),
                  'L':(i-1),
                  'D':(i+3),
                  'U':(i-3)}
   print(validMoves)
   return validMoves

def checkIfExplored(node, table):
   return (str(node) in table.values())

#AStar Algorithim
def aStar(start, goal):
   #begin = start.index(0)
   frontier = pq()
   frontier.insert(start)
   #totalG = 0
   #totalH = get initial hVal from aHeuristic

   explored = {}
   hashToTable(explored, start)

   #while frontier.empty() != True:
   currNode = frontier.peek()
   if currNode == goal:
      #we want to add in a function to reconstruct the path
      return "Goal found"
      #pass
   #how do we get the previously moved value?
   #totalG = totalG + goal(currNode)
   expanding = frontier.remove()
   hashToTable(explored, expanding)
   possibleMoves = checkPossibleMoves(currNode)
   print('current: ',currNode)
   for move in possibleMoves.values():
      #here we need to evaluate the g score of the move, add in the g score to be considered in the below if statement
      if move <= 8 and move >= 0:
         moveVal = currNode.index(move)
         print('move ', move, ': ')
         addNewNode = testMove(move, currNode)
         if checkIfExplored(addNewNode, explored) is False:
            frontier.insert(addNewNode)
            hashToTable(explored, addNewNode)
      #Check for the smallest g score to add to a list of previous nodes, so we can add to the total g for printing
   return "Not found"

def main():
   print("test")
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
   main()
   aStar(initArr, goalArr)
