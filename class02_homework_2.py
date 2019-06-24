#Fibonacci --- Recursion+For
def fibonacci(i): #定義費氏函數
    if (i==0 or i==1): #若費式數列輸入值為0或1
        return i #則回傳0或1
    else:
        return fibonacci(i-1)+fibonacci(i-2) #輸入值為其他數則回傳前兩項相加的運算結果
max=int(input('Fibonacci 第n項數值:')) #輸入費式數列最後一項
for i in range(0,max+1): 
    Fib=fibonacci(i) #呼叫函式並回傳費式數列值  
    if i==0 or i==1: #數列前兩項輸出格式和後面項次不同
        print('Fib('+str(i)+')'+'='+str(Fib))
    else:
        print('Fib('+str(i)+')'+'=Fib('+str(i-1)+')'+'+Fib('+str(i-2)+')='+str(Fib))