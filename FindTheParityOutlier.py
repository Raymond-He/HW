def find_outlier(integers):
    even=[]
    odd=[]

    for i in integers:
        if i%2==0:
            even.append(i) #偶
        else:
            odd.append(i) #奇

    if len(even)==1: 
        return even[0] #回傳偶數
        
    if len(odd)==1:
        return odd[0] #回傳奇數

#  測試
print(find_outlier([2, 4, 6, 8, 10, 3]))				#, 3)
# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))	#, 11)
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))	#, 160)