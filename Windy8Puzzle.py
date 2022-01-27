#Ryan Schanerberger & Alexis Tucker
#CIS 479
#Windy 8-Puzzle
from array import*
from heapq import*
import itertools
import queue

#pq = array('i', []);

class pq:
   def __init__(self):
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
<<<<<<< Updated upstream
   #prints if queue is empty
   def isEmpty(self):
      return len(self.minHeap) == True
=======
      return popped
>>>>>>> Stashed changes
   #need to full print heap
   def printHeap(self):
      for i in self.minHeap:
            print(i, end = ' ')
            print()
         

heapObj = pq()
heapObj.insert(3)
heapObj.insert(2)
heapObj.insert(15)
heapObj.insert(5)
heapObj.insert(4)
heapObj.insert(45)
heapObj.remove()
   
#print(heapObj.peek())

#heapObj.printHeap()

#print(heapObj.isEmpty())

<<<<<<< Updated upstream
#heapObj.remove()
#heapObj.remove()

=======
>>>>>>> Stashed changes
#heapObj.printHeap()

class aGraph:
   def __init__(self, edges, n):
      self.adj = [[] for _ in range(n)]
      
      for(s, d) in edges:
         self.adj[s].append(d)
#Add vertex to adjacency list
   def addVertex(self, v):
      if v not in self.adj:
         self.adj[v] = []
#Add an edge
   def addEdge(self, edge):
      edge = set(edge)
      (v1, v2) = tuple(edge)
      if v1 in self.gDict:
         self.gDict[v1].append(v2)
      else:
         self.gDict[v1] = [v2]
   def swapVertex(self, v1, v2):
      swapped = False
      if self.adj[v1] != 0 and self.adj[v2] != 0:
         x = self.adj[v1]
         y = self.adj[v2]
         self.adj[v2] = x
         self.adj[v1] = y
         swapped = True
      return swapped
            
#List the edges of graph
   def findEdges(self):
      edgename = []
      for vx in self.gDict:
         for nxtvx in self.gDict[vx]:
            if {nxtvx, vx} not in edgename:
               edgename.append({vx, nxtvx})
      return edgename
#print the adjacency matrix
   def printGraph(self):
    for src in range(len(self.adj)):
        for dest in self.adj[src]:
            if dest == 0 or src == 0:
               print(f'( - —> {dest}) ', end='')
            else:
               print(f'({src} —> {dest}) ', end='')
        print()

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
<<<<<<< Updated upstream
initialSt = [(2, 8), (2, 6), (8, 2), (8, 3),(8,7), (3,8), (3,4), (7, 6), (7,8), (7, 4), (7,5), (4, 7), (4, 3), (4, 0),
 (1, 6), (1,5), (5, 1), (5, 7), (5,0), (0,5), (0,4)]

numOfVertices = 9

g = aGraph(initialSt, numOfVertices)
=======
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
>>>>>>> Stashed changes
#print(g.getVertices())
#print(g.getEdges())

#g.printGraph()

print(g.swapVertex(1, 2))

g.printGraph()

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

   

def blah():
   for i in range(len(goal)):
      print("Finding", i, ":")
      while i != current[j]:
         if(j == 8):
            j = 0
         count = count + 1
         print(count, end = ' ')
         j = j + 1
      count = 0
      j = 0
      print()


