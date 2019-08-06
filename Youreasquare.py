def is_square(n):    
    import math
    
    if n<0: #負數
        return False

    sqrt=int(math.sqrt(n)) #找n的平方根
    if sqrt*sqrt == n: #平方根相乘==n
        return True #即平方數
    else:
        return False

# 測試
# test.describe("is_square")
# test.it("should work for some examples")
print(is_square(-1))            # , False, "-1: Negative numbers cannot be square numbers")
print(is_square( 0))            # , True, "0 is a square number")
print(is_square( 3))            # , False, "3 is not a square number")
print(is_square( 4))            # , True, "4 is a square number")
print(is_square(25))            # , True, "25 is a square number")
print(is_square(26))            # , False, "26 is not a square number")