class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its time to reach the target
        cars = sorted(zip(position, speed), reverse=True)
        times = [(target - p) / s for p, s in cars] # Time = distance / speed
        
        fleets = 0 
        curr_time = 0 
        for t in times:
            if t > curr_time: 
                fleets += 1 
                curr_time = t 
        
        return fleets # number of fleets 