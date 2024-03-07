def isHappy(self, n: int) -> bool:
    my_set = set()
    def square_n(n):
        n = str(n)
        new = 0
        for char in n:
            new += int(char) ** 2
        return new
    
    while n not in my_set:
        my_set.add(n)
        n = square_n(n)
        if n == 1:
            return True