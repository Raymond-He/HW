length=int(input('請輸入長寬大小:')) #決定長寬大小
length=length//2 #做左半邊
#上半部
for i in range(0,length): #依序從左半邊到中間
    odd=2*i-1 #決定星號間的空白為奇數(從小排到大)
    blank=length-i #決定星號前的空白
    if odd<0: #如果星號間的空白<0
        print(blank*' '+"*") #印出最上面的星號
    else:
        print(blank*' '+"*"+odd*' '+"*") #剩下的都印出星號前的空白+星號+星號間的空白+星號
#下半部
for j in range(0,length+1): #依序從左半邊到中間
    oddblank=2*j+1 #決定星號間的空白為奇數
    frontblank=j #決定星號前的空白
    oddblankI=2*length-oddblank #星號間的空白數(從大排到小)
    if oddblankI<0: #如果星號間的空白<0
        print(frontblank*' '+"*") #印出最下方的星號
    else:
        print(frontblank*' '+"*"+oddblankI*' '+"*") #剩下的都印出星號前的空白+星號+星號間的空白+星號