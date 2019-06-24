Matrix=[] #宣告質數放的矩陣
Max=int(input("輸入最大範圍:"))
for i in range(1,Max+1):
    Buffer=[] #讀入新數字時先清空暫存
    for j in range(1,i+1): #因數為1到自己
        if i%j==0: #若讀入的數字和因數取餘數==0
            Buffer.append(j) #把因數j放入暫存
    if len(Buffer)==2: #若暫存長度==2，則表示只有1和自己 =質數
        Matrix.append(i) #把質數放入矩陣
print(Matrix) #印出使暫存長度為2的數字 =質數