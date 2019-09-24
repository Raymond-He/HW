def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return '{0[0]} likes this'.format(names)
    if len(names) == 2:
        return '{0[0]} and {0[1]} like this'.format(names)
    if len(names) == 3:
        return '{0[0]}, {0[1]} and {0[2]} like this'.format(names)
    if len(names) >= 4:
        return "{0[0]}, {0[1]} and {people} others like this".format(names, people = len(names)-2)

# 測試
print(likes([]))									#, 'no one likes this')
print(likes(['Peter']))							#, 'Peter likes this')
print(likes(['Jacob', 'Alex']))					#, 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']))				#, 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))	#, 'Alex, Jacob and 2 others like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Bye']))	#, 'Alex, Jacob and 3 others like this')