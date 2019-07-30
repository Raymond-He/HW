def max_multiple(divisor, bound):
    x=[]
    if bound<divisor: #邊界小於除數回傳0
        return 0
    
    else:
        for i in range(0,bound+1): 
            if i%divisor==0: #找0~bound內divisor的倍數
                x.append(i) #丟入暫存的x陣列
        return max(x) #印出陣列內最大值

# 測試
# Test.describe("Basic tests")
# print(max_multiple(2,7))     #  ,6)
# print(max_multiple(3,10))     #  ,9)
# print(max_multiple(7,17))     #  ,14)
# print(max_multiple(10,50))    #  ,50)
# print(max_multiple(37,200))   #  ,185)
print(max_multiple(7,100))    #  ,98)
# print(max_multiple(37,100))   #  ,74)
# print(max_multiple(1,13))     #  ,13)
# print(max_multiple(1,1))	     #  ,1)
# print(max_multiple(4,1))	     #  ,0)
# print("<COMPLETEDIN::>")