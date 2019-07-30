def reverseWords(str):
    StringSplit=str.split() # 字串切割
    StringReverse=StringSplit[::-1] #字串反轉
    results = ' '.join(i for i in StringReverse) #字串相加
    return results
    
#  測試
print(reverseWords("The greatest victory is that which requires no battle"))
# // should return "battle no requires which that is victory greatest The"