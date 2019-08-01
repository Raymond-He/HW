def row_weights(array):
    even=[]
    odd=[]
    sumeven=sumodd=0
    for i in range(0,len(array)):
        if i%2==0:
            even.append(array[i]) #陣列偶數位置
        else:
            odd.append(array[i]) #陣列奇數位置
    for x in even:
        sumeven+=x #偶數陣列值相加
    for y in odd:
        sumodd+=y #奇數陣列相加
    z=(sumeven,sumodd)
    return tuple(z) #list 轉成 tuple

# 測試
# Test.describe("Basic tests")
#print(row_weights([80]))					    #, (80,0)
# print(row_weights([100,50]))					#, (100,50))
# print(row_weights([50,60,70,80]))				#, (120,140))
#print(row_weights([13,27,49]))					#, (62,27))
# print(row_weights([70,58,75,34,91]))			#, (236,92))
# print(row_weights([29,83,67,53,19,28,96]))		#, (211,164))
# print(row_weights([0]))						#, (0,0))
#print(row_weights([100,51,50,100]))			#, (150,151))
print(row_weights([39,84,74,18,59,72,35,61]))	#, (207,235))
#print(row_weights([0,1,0]))					#, (0,1))