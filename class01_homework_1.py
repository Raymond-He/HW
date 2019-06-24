from random import * #引入random函式

blank=[] #宣告20個數字放的陣列
time=1 #決定迴圈做幾次的參數
while time<=20: #總共取出20個數字
    random=randint(1,201) #從1~200隨機挑
    if random not in blank: #若隨機挑的值不在陣列中
        blank.append(random) #把不在陣列中的值放進陣列內(避免重複)
        time=time+1 #做完以上動作再從1~200隨機挑一個值

print(blank) #印出挑完20個不重覆數字的陣列

blankI=[] #宣告二位數字放的陣列
for i in blank: #將先前取出的20個數字依序放入i
    if i<100 and i>=10: #若放入的20個數字10=<i<100，則一定為二位數
        blankI.append(i) #把二位數的值放入新的陣列
        
print(blankI) #印出二位數的陣列

odd=[] #奇數
even=[] #偶數
for j in blankI: #把剛才挑出的二位數依序放入j
    if j%2==1: #若j mod 2為1
        odd.append(j) #則放入奇數
    else:
        even.append(j) #若取餘數不為1則放入偶數

print('odd='+str(odd)) #印出奇數
print('even='+str(even)) #印出偶數