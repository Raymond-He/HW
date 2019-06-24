num=[] #放質數的陣列
for dividend in range(2,101): #決定被除數的範圍
   for divisor in range(2,dividend): #讓除數從開始值到現在正在運算的值
      if dividend%divisor==0: #如果正在運算的值和比自己小的值取餘數為0(代表整除)
        break #就跳出這個for迴圈`,不執行下面的else,並挑下一個數字來做運算
   else:
      num.append(dividend) #如果正在運算的值和比自己小的數字取餘數不為0則為質數

print(num) #印出質數