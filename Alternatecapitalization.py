def capitalize(s):
    even = []
    odd = []
    result = []

    for i in range(0,len(s)):
        if i % 2 == 0: #偶數位置
            even.append(s[i].upper()) #放到even變大寫
            odd.append(s[i]) #放到odd變小寫
        else: #奇數位置
            even.append(s[i]) #放到even變小寫
            odd.append(s[i].upper()) #放到odd變大寫
            
    result.append(''.join(even)) 
    result.append(''.join(odd))
    return result

# 測試
# Test.it("Basic tests")
print(capitalize("abcdef"))				#,['AbCdEf', 'aBcDeF'])
print(capitalize("codewars"))				#,['CoDeWaRs', 'cOdEwArS'])
print(capitalize("abracadabra"))			#,['AbRaCaDaBrA', 'aBrAcAdAbRa'])
print(capitalize("codewarriors"))			#,['CoDeWaRrIoRs', 'cOdEwArRiOrS'])