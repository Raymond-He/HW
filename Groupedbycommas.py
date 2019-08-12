def group_by_commas(n):
    return str(format(n,',')) #數字千分符

print(group_by_commas(1))				#, '1')
print(group_by_commas(10))			#, '10')
print(group_by_commas(100))			#, '100')
print(group_by_commas(1000))			#, '1,000')
print(group_by_commas(10000))			#, '10,000')
print(group_by_commas(100000))		#, '100,000')
print(group_by_commas(1000000))		#, '1,000,000')
print(group_by_commas(35235235))		#, '35,235,235')