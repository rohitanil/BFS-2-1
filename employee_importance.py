"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque
"""
Time complexity -> O(N) where N is the number of elements in employee list
Space Complexity -> O(N)
Logic:
We create an adjacency list of id to Employee object. This is used to easily compute the importance and
navigate to next nodes. When building the adjacency list, insert the employee id that we have to compute the importance. This will
act as the starting node for BFS traversal
Do a BFS traversal and at each child node, add to the importance variable which was initially set to 0.
Return importance variable.
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adj_list = {}
        queue = deque()
        for emp in employees:
            adj_list[emp.id] = emp
        queue.append(adj_list[id])
        imp = 0
        while queue:
            emp_obj = queue.popleft()
            imp += emp_obj.importance
            for sub in emp_obj.subordinates:
                queue.append(adj_list[sub])
        return imp
