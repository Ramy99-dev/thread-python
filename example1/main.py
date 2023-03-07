import heapq
from task1 import counter
from task2 import simplePrint
from task3 import getData


tasks = {int(input("Give task priority :")) : counter ,
         int(input("Give task priority :")) : simplePrint ,
         int(input("Give task priority :")) : getData 
        }

aux = list(tasks.items())
heapq.heapify(aux)

print(aux)

tasks = dict(aux)
print(tasks)
for i in range(0,3):
    leastElement = heapq.heappop(aux)
    leastElement = list(leastElement)
    leastElement[1]()

