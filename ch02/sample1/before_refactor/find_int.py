class FindInt:
    @staticmethod
    def find(data: int, target: int)  -> bool:
        flag = False
        i = 0
        while i < len(data) and not flag:
            if data[i] == target:
                flag = True
            i += 1
        return flag