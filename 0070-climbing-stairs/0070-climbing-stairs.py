class Solution(object):
    def climbStairs(self, n):
        climb_map = {1: 1, 2: 2}
        if n <= 2:
            return climb_map[n]
        
        for i in range(3, n+1):
            climb_map[i] = climb_map[i-1] + climb_map[i-2] 
        
        return climb_map[n]