#Fibonacci --- For
n=int(input('Fibonacci 第n項數值:')) #輸入費式數列最後一項
first=second=0 #設定數列初始值
for time in range(0,n+1): #決定數列共跑幾項
    if time==2: #在跑Fib(2)時強制設定第一項為0，第二項為1
        first=0
        second=1
    third=first+second #第三項的值為第一二項的相加
    first=second #做完相加後把第一項的值用第二項覆蓋
    second=third #第二項的的值用第三項的值覆蓋
    if time==0 or time==1: #數列前兩項輸出格式和後面項次不同
        print('Fib('+str(time)+')='+str(third))
    else:
        print('Fib('+str(time)+')=Fib('+str(time-1)+')+Fib('+str(time-2)+')='+str(third))
    if first==0 and second==0: #第一二項原來為0，為了使費式數列開始運算，第二項的值必須輸入1
        second+=1