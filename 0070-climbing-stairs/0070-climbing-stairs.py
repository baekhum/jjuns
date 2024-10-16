class Solution(object):
    def climbStairs(self, n, climb_map = {}):
        if n not in climb_map:
            if n < 3:
                return n
            climb_map[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2) 
        return climb_map[n]