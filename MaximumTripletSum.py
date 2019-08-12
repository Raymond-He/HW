def max_tri_sum(numbers):
    # ==================================法二===================================
    buf_max=[]
    maximum=[]

    numbers=sorted(list(set(numbers))) #排序(tuple變清單(刪重複的))
    numbers.reverse() #反轉

    for i in range(0,3): #取前三大值
        buf_max=numbers.pop(0)
        maximum.append(buf_max)
    return sum(maximum)
    # =========================================================================

    # ============================法一===========================
    # numbers=sorted(numbers)

    # buf_max=[]
    # maximum=[]

    # delduplicates=[] #刪掉重複
    # for first in range(len(numbers)): #陣列0和
    #     for second in range(first+1,len(numbers)): #之後的陣列元素做比較
    #         if numbers[second] == numbers[first]: #遇到重複值跳出迴圈
    #             break
    #         else:
    #             if second == len(numbers)-1: #沒有值重複
    #                 delduplicates.append(numbers[first]) #存放唯一值
    # delduplicates.append(numbers[first]) #印出所有唯一值
    
    # delduplicates.reverse()
    # for i in range(0,3): #取前三大值
    #     buf_max=delduplicates.pop(0)
    #     maximum.append(buf_max)
    # return sum(maximum)
    # ===========================================================

# 測試
# Test.describe("Basic tests")
print(max_tri_sum([3,2,6,8,2,3]))						#,17)
print(max_tri_sum([2,9,13,10,5,2,9,5]))				#,32)
print(max_tri_sum([2,1,8,0,6,4,8,6,2,4]))				#,18)
print(max_tri_sum([-3,-27,-4,-2,-27,-2]))				#,-9)
print(max_tri_sum([-14,-12,-7,-42,-809,-14,-12]))		#,-33)
print(max_tri_sum([-13,-50,57,13,67,-13,57,108,67]))	#,232)
print(max_tri_sum([-7,12,-7,29,-5,0,-7,0,0,29]))		#,41)
print(max_tri_sum([-2,0,2]))							#,0)
print(max_tri_sum([-2,-4,0,-9,2]))					#,0)
print(max_tri_sum([-5,-1,-9,0,2]))					#,1)
# print("<COMPLETEDIN::>")