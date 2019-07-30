def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0: #計算元素出現次數
            return i # i為出現奇數次的數字

# 測試
# test.describe("Example")
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))		#, 5)