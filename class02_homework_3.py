def sort_array(a): #定義排序函式
    odd=[] #奇數陣列
    even=[] #偶數陣列
    sortArrayI=[] #最後結果放的陣列
    for i in a: #先將原始陣列依序讀入
        if i%2==0: #若為偶數放入even陣列
            even.append(i)
        else: #若為奇數則放入odd陣列
            odd.append(i)
    sorting=sorted(odd) #奇數陣列由小排到大
    reversing=sorted(even, reverse =True) #偶數陣列由大排到小

    time=timer=0 #決定取奇偶陣列中的第幾個
    for num in range(0,len(a)): #判斷原始陣列大小
        if a[num]%2!=0: #若原始陣列內的數值為奇數
            while time <= len(sorting): #判斷奇數陣列的大小
                sortArrayI.append(sorting[time]) #從奇數陣列取最小值放入
                time+=1 #下一次則取第二小的奇數放入要印出的矩陣
                break #放入一個值後就跳出迴圈，繼續判斷原始陣列的下一個值是奇數或偶數
        else: #若原始陣列內的數值為偶數
            while timer <= len(reversing): #判斷偶數陣列的大小 
                sortArrayI.append(reversing[timer]) #從偶數陣列取最大值放入
                timer+=1 #下一次則取第二大的偶數放入要印出的矩陣
                break #放入一個值後就跳出迴圈，繼續判斷原始陣列的下一個值是奇數或偶數
    return sortArrayI #回傳結果
Final_Array=sort_array([5,3,2,8,1,4]) #輸入原始矩陣並呼叫函數做完運算後
print(Final_Array) #印出結果