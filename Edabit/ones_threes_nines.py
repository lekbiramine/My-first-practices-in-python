class ones_threes_nines:
    def __init__(self,whole_num):
        self.whole_num = whole_num
        self.ones = whole_num // 1
        self.threes = whole_num // 3
        self.nines = whole_num // 9
    
n1 = ones_threes_nines(5)
print(n1.ones)
print(n1.threes)
print(n1.nines)