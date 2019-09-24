def persistence(n):
    time = 0
    count = 0 #乘幾次
    buflen = len(str(n)) #暫存字串長度

    if n < 10: 
        return 0
    else:
        while time <= buflen:
            nlist = list(map(int,str(n))) #list(字串元素轉整數元素(數字轉字串))
            
            multi = 1
            for i in nlist: #list內值相乘
                multi *= i

            n = multi 
            count += 1 #做一次相乘

            if n < 10:
                break
            time += 1

        return count

# 測試
# Test.it("Basic tests")
print(persistence(39))			#, 3)
print(persistence(4))           #, 0)
print(persistence(25))			#, 2)
print(persistence(999))			#, 4)
print(persistence(9999))	    #, 3)