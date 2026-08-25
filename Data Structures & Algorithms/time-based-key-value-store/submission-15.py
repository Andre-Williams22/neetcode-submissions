class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # key value insertion lookup and insertion 
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp]) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        # hashtable.get() the key value 
        listValues = self.store[key]
        # Binary search for the largest timestamp <= given timestamp
        l, r = 0, len(listValues) - 1 
        result = ""
        while l <= r:
            mid = (l + r)//2 
            # look for largest timestamp
            if listValues[mid][1] <= timestamp:
                result = listValues[mid][0] # candidate answer
                l = mid + 1 # try to find later timestamp
            else:
                r = mid - 1 # search left half  

        return result 