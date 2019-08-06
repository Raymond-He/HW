def order(sentence):
    buffer=[]
    results=[]

    for i in sentence.split(" "): #變成list
        import re
        buffer.append((re.findall("\d",i),i)) #數字帶字串

    for j in sorted(buffer): #排序數字等於排序字串
        results.append(j[1]) #取字串
    return ' '.join(results) #陣列轉str

# 測試
print(order("is2 Thi1s T4est 3a"))                # , "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"))  # , "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""))                                  # , "")
