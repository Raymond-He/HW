def duplicate_count(text):
    text = text.lower() #變小寫
    textlist = list(set(text)) #砍重複
    result = 0

    for i in textlist:
        if text.count(i) > 1: #抓出重複
            result +=1
            
    return result

# 測試
# print(duplicate_count("abcde"))			#, 0)
print(duplicate_count("abcdea"))			#, 1)
print(duplicate_count("indivisibility"))	#, 1)
print(duplicate_count("indivisibilityD"))	#, 2)