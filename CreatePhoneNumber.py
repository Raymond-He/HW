def create_phone_number(n):
    LocalNumber=[] #區碼
    FrontPhoneNumber=[] #前3碼
    BackPhoneNumber=[] #後4碼

    for i in range(0,3): #[0:4]
        LocalNumber.append(n[i]) #丟入區碼陣列

    for j in range(3,6):
        FrontPhoneNumber.append(n[j]) #丟入前三碼陣列

    for k in range(6,10):
        BackPhoneNumber.append(n[k]) #丟入後四碼陣列

    # 回傳電話
    return ("("+str(LocalNumber[0])+str(LocalNumber[1])+str(LocalNumber[2])+") "+str(FrontPhoneNumber[0])+str(FrontPhoneNumber[1])+str(FrontPhoneNumber[2])+"-"+str(BackPhoneNumber[0])+str(BackPhoneNumber[1])+str(BackPhoneNumber[2])+str(BackPhoneNumber[3]))

# 測試
# print(create_phone_number("Basic tests))
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) #(123) 456-7890
# print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) #(111) 111-1111
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])) #(023) 056-0890
# print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) #(000) 000-0000
