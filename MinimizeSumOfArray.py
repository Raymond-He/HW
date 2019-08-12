def min_sum(arr):
    arr=sorted(arr) #arr排序
    multi1=multi2=plus=[] #乘數、被乘數、待加處
    time = 0
    buflength = len(arr) #存放arr長度

    while time < (buflength/2): 
        multi1=arr.pop(0) 
        multi2=arr.pop(len(arr)-1)
        plus.append(multi1*multi2) #頭*尾
        time+=1

    return sum(plus) #待加處相加結果

# 測試
# Test.describe("Basic Tests")
# Test.it("should return the minimum sum")
print(min_sum([5,4,2,3]))			 # , 22)
print(min_sum([12,6,10,26,3,24]))  # , 342)
print(min_sum([9,2,8,7,5,4,0,6]))  # , 74)
