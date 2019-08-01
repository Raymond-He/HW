def min_value(digits):
    delduplicates=[] #刪掉重複
    for first in range(len(digits)): #陣列0和
        for second in range(first+1,len(digits)): #之後的陣列元素做比較
            if digits[second] == digits[first]: #遇到重複值跳出迴圈
                break
            else:
                if second == len(digits)-1: #沒有值重複
                    delduplicates.append(digits[first]) #存放唯一值
    delduplicates.append(digits[first]) #印出所有唯一值

    # len(delduplicates)=4
    for i in range(0,len(delduplicates)-1): #有n-1回合(n為數字個數) 0 1 2
        for j in range(0,len(delduplicates)-1-i): #每回合進行比較的範圍 0-3 0-2 0-1
            if delduplicates[j] > delduplicates[j+1]: #是否需交換
                tmp = delduplicates[j]
                delduplicates[j] = delduplicates[j+1]
                delduplicates[j+1] = tmp
    string = ''.join(str(i) for i in delduplicates) #數字陣列轉字串
    return int(string)

# 測試
# print(min_value([1, 3, 1]))				    #, 13)
# print(min_value([4, 7, 5, 7]))				#, 457)
# print(min_value([4, 8, 1, 4]))				#, 148)
print(min_value([1, 9, 3, 1, 7, 4, 6, 6, 7])) #, 134679)
