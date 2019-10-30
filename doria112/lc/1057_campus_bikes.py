class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # calculate distance for each pair of worker and bike
        # store the results in a list of tuples (distance, worker, bike) 
        # sort the tuples, which takes care of the priority of distance, worker, then bike
        # process from the left most until all workers are assigned with a bike
        
        # time complexity O(mn*log(mn))
        # m - length of workers
        # n - length of bikes
        
        assigned_bikes = [0] * len(workers)
        
        pri = []
        
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                dis = abs(w[0] - b[0]) + abs(w[1] - b[1])
                pri.append((dis, i, j))
        
        pri = sorted(pri)
        
        done_workers = set()
        done_bikes = set()
        
        for p in pri:
            if len(done_workers) == len(workers):
                return assigned_bikes
            if p[1] in done_workers:
                continue
            if p[2] in done_bikes:
                continue
            assigned_bikes[p[1]] = p[2]
            done_workers.add(p[1])
            done_bikes.add(p[2])
    
        return assigned_bikes
