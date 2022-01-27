#Ryan Schanerberger & Alexis Tucker
#CIS 479
#Windy 8-Puzzle
from array import*
from heapq import*
import itertools
import queue

#pq = array('i', []);

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
         



heapObj = pq()
heapObj.insert(2)
heapObj.insert(3)
heapObj.insert(15)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(45) 
   
#print(heapObj.peek())

#heapObj.printHeap()

heapObj.remove()
heapObj.remove()

#heapObj.printHeap()

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

#g = aGraph(initialSt)
#print(g.getVertices())
#print(g.getEdges())

#print(goalArr)

myTup = (1, 2, 3, 4)

test = 'T2'

num = 1000

def hashToTable(table, member):
   hashVal = hash(member)
   table[member] = [hashVal]

hashTable = {}

hashToTable(hashTable, myTup)
hashToTable(hashTable, test)
hashToTable(hashTable, num)

print(hashTable)

#=================================================================#
#note for the hVal: up == 1, down == 3, left == 2, right == 2#
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
      print(hVal)
      print()

         

aHeuristic(initArr, goalArr)


