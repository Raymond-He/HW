def solve(arr): 
    x=[] #存放結果
    for first in range(len(arr)): #陣列0和
        for second in range(first+1,len(arr)): #之後的陣列元素做比較
            if arr[second] == arr[first]: #遇到重複值跳出迴圈
                break
            else:
                if second == len(arr)-1: #沒有值重複
                    x.append(arr[first]) #存放唯一值
    x.append(arr[first]) #印出所有唯一值
    return x

# 測試
# Test.it("Basic tests")
# print(solve([3,4,4,3,6,3]))		#,[4,6,3])
# print(solve([1,2,1,2,1,2,3]))	    #,[1,2,3])
# print(solve([1,2,3,4]))			#,[1,2,3,4])
print(solve([1,1,4,5,1,2,1]))	    #,[4,5,2,1])