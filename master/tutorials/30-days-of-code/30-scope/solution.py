    def computeDifference(self):
        if(a is None or len(a) == 0):
            raise Exception('Elements null or empty', a)
        self.maximumDifference = abs(max(a) - min(a))