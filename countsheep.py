def count_sheep(n):
    results=[]
    for num in range(1,n+1):
        results.append(str(num)+" sheep...") #字串放陣列
    return ''.join(results) #陣列轉字串

# 測試
print(count_sheep(1))        #, "1 sheep...");
print(count_sheep(2))        #, "1 sheep...2 sheep...")
print(count_sheep(3))        #, "1 sheep...2 sheep...3 sheep...")