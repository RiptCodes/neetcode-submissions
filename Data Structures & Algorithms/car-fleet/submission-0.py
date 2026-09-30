class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_time = 0
        fleets = 0
        sort_cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in sort_cars:
            time = (target - pos) / spd
            if time > fleet_time:
                fleets += 1
                fleet_time = time

        return fleets
        