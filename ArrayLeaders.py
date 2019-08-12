def array_leaders(numbers):
    compare=[]
    results=[]

    time = 0
    buflennum = len(numbers) #暫存numbers的長度

    while time < buflennum:
        compare=numbers.pop(0) #提出numbers[0]

        if compare > sum(numbers): #若大於剩下numbers總和，印出
            results.append(compare)

        time+=1
    return results

# 測試
# Test.describe("Sample Tests")
# Test.it("Positive Values")
print(array_leaders([1,2,3,4,0]))			#, [4])
print(array_leaders([16,17,4,3,5,2]))		#, [17,5,2])
                                            
# Test.it("Negative Values")                  
print(array_leaders([-1,-29,-26,-2]))		#, [-1])
print(array_leaders([-36,-12,-27]))		#, [-36,-12])
                                            
# Test.it("Mixed Values")                     
print(array_leaders([5,2]))				#, [5,2])
print(array_leaders([0,-1,-29,3,2]))		#, [0,-1,3,2])