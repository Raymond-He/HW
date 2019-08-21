def bowling_pins(arr):
    result = ""

    complete = "I I I I\n I I I \n  I I  \n   I   " #全在版
    complete = list(complete) #轉成list

    for i in arr: #取代
        if i == 1:
            complete[27] = " "
        elif i == 2:
            complete[18] = " "
        elif i == 3:
            complete[20] = " "
        elif i == 4:
            complete[9] = " "
        elif i == 5:
            complete[11] = " "
        elif i == 6:
            complete[13] = " "
        elif i == 7:
            complete[0] = " "
        elif i == 8:
            complete[2] = " "
        elif i == 9:
            complete[4] = " "
        else:
            complete[6] = " "

    for j in complete: #轉回str
        result += j
    return result

# ================================anter69=====================================
# def bowling_pins(arr):
#     pins =  "7 8 9 0\n" + \
#             " 4 5 6 \n" + \
#             "  2 3  \n" + \
#             "   1   "
    
#     for i in range(1, 11): #直接取代字串1~0
#         if i in arr:
#             pins = pins.replace(str(i%10), " ")
#         else:
#             pins = pins.replace(str(i%10), "I")
    
#     return pins

# ================================Indiradri, HubHaz=========================================
# def bowling_pins(arr):
#     pins = [7,8,9,10,4,5,6,2,3,1]
#     pins_after= []
#     for pin in pins:
#         if pin in arr:
#             pins_after.append(' ')
#         else:
#             pins_after.append('I')

#     return '{} {} {} {}\n {} {} {} \n  {} {}  \n   {}   '.format(*pins_after) #判斷好的list用format放回

# 測試
print(bowling_pins([2,3]))		#, "I I I I\n I I I \n       \n   I   ")
print(bowling_pins([1,2,10]))	    #, "I I I  \n I I I \n    I  \n       ")
print(bowling_pins([8,2,7]))