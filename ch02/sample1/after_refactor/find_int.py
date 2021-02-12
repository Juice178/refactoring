class FindInt:
    @staticmethod
    def find(data: int, target: int)  -> bool:
        for i in range(len(data)):
            if data[i] == target:
                return True 
        return False