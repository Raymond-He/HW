def iq_test(numbers):
    even=[]
    odd=[]

    results = list(map(int,numbers.split())) #list中的string轉成int

    for i in results:
        if i%2==0:
            even.append(i) #偶
        else:
            odd.append(i) #奇

    if len(even)>len(odd): # 偶組---找奇
        return results.index(odd[0])+1 #list中第一次出現該元素的位置
    else: # 奇組---找偶
        return results.index(even[0])+1

# 測試
# print(iq_test("2 4 7 8 10"))	# ,3)
print(iq_test("1 2 2"))		# ,1)