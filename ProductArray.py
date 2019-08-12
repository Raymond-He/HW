def product_array(numbers):
    buf_numbers=numbers[:] #陣列複製
    ignore=[]
    results=[]

    for i in range(0,len(buf_numbers)):
        numbers=buf_numbers[:] #陣列複製
        ignore=numbers.pop(i) #依次取走陣列0~len(buf_numbers)位置的值
        
        product = 1
        for x in numbers: 
            product *= x #待乘清單所有值相乘
        results.append(product)

    return results

# 測試
# Test.describe("Basic Tests")
print(product_array([12,20]))				#, [20,12])
print(product_array([12,20]))				#, [20,12])
print(product_array([3,27,4,2]))			#, [216,24,162,324]) 216=27*4*2
print(product_array([13,10,5,2,9]))		#, [900,1170,2340,5850,1300])
print(product_array([16,17,4,3,5,2]))		#, [2040,1920,8160,10880,6528,16320])
# print("<COMPLETEDIN::")