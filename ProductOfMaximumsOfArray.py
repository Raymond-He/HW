def max_product(lst, n_largest_elements):
    productlist=[] #待乘清單

    lst=sorted(lst) #由小到大
    lst.reverse() #由大到小

    for j in range(0,n_largest_elements): 
        productlist.append(lst[j]) #前幾大的數字放到待乘清單
    
    product = 1
    for x in productlist: 
        product *= x #待乘清單所有值相乘
    return product

# 測試
# Test.it("Basic Tests")
print(max_product([0]*10, 5))			#, 0)
print(max_product([4,3,5], 2))		#, 20)
print(max_product([10,8,7,9], 3))		#, 720)
print(max_product([8,6,4,6], 3))		#, 288)

# Test.it("Larger arrays")
print(max_product (list(range(10, -1, -1)), 5))				#, 10*9*8*7*6)
print(max_product ([10,2,3,8,1,10,4], 5))						#, 9600)
# print(max_product ([13,12,-27,-302,25,37,133,155,-1], 5))		#, 247895375)
             
# Test.it("Arrays with negative values")
# print(max_product ([-4,-27,-15,-6,-1],2))		#, 4)
# print(max_product ([-17,-8,-102,-309],2))		#, 136)
             
# Test.it("Arrays with positive and negative values")
# print(max_product ([10,3,-27,-1], 3))				#, -30)
# print(max_product ([14,29,-28,39,-16,-48],4))		#, -253344)