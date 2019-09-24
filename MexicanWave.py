def wave(str):
    str = list(str) #字串轉list
    result = []
    strcopy = str[:] #list data buffer

    for i in range(0,len(str)):
        if str[i] == ' ': #排除空白
            pass
        else:
            str[i] = str[i].upper() #一個一個值變大寫
            result.append(''.join(str)) #加到結果中
            str = strcopy[:] #恢復到原始的strlist
            
    return result

# 測試
# result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# test.it("Should return: '["+", ".join(result)+"]'")
print(wave("hello"))									    #, result)

# result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
# test.it("Should return: '["+", ".join(result)+"]'")
print(wave("codewars"))									#, result)

# result = []
# test.it("Should return: '["+", ".join(result)+"]'")
print(wave(""))											#, result)

# result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
# test.it("Should return: '["+", ".join(result)+"]'")
print(wave("two words"))								    #,result)

# result = [" Gap ", " gAp ", " gaP "]
# test.it("Should return: '["+", ".join(result)+"]'")
print(wave(" gap "))									    #, result)