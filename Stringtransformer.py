def string_transformer(s):
    reverse = s.split(' ')[::-1] #字串轉清單[反轉]
    string = ' '.join(reverse) #清單轉字串
    return string.swapcase() #大小寫互換

# 測試
print(string_transformer("Example string"))									#, "STRING eXAMPLE")
print(string_transformer("Example Input"))									#, "iNPUT eXAMPLE")
print(string_transformer("To be OR not to be That is the Question"))			#, "qUESTION THE IS tHAT BE TO NOT or BE tO")

# Should handle empty string                                                    
print(string_transformer(""))													#, "")

# Should handle multiple spaces                                                 
print(string_transformer("You Know When  THAT  Hotline Bling"))				#, "bLING hOTLINE  that  wHEN kNOW yOU")

# Should handle leading space                                                   
print(string_transformer(" A b C d E f G "))									#, " g F e D c B a ")