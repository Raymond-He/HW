def number_of_pairs(gloves):
    gloveslist = list(set(gloves)) #砍重複
    result = []

    for i in gloveslist:
        result.append(gloves.count(i) // 2) #算幾對手套

    return sum(result)

# 測試
# Test.describe("Basic tests")
print(number_of_pairs(["red","red"]))														#,1)
print(number_of_pairs(["red","green","blue"]))											#,0)
print(number_of_pairs(["gray","black","purple","purple","gray","black"]))					#,3)
print(number_of_pairs([]))																#,0)
print(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]))		#,4)