def name_in_str(str, name):
    character=[]
    strlist=[]
    name_pop=[]

    for i in name.lower():
        character.append(i) #name轉成一個一個字元+變小寫

    for j in str.lower():
        strlist.append(j) #string通通變成小寫

    name_pop=character.pop(0) #character放到一個到判斷

    for x in range(len(strlist)): #str一個一個拿出來
        if strlist[x] == name_pop[0]: #str等於name_pop
            if len(character) != 0: 
                name_pop=character.pop(0) #character再放到一個到判斷

            else: #len(character)==0 and strlist[x] == name_pop[0]
                return True
    return False #strlist[x] != name_pop[0]

# Test.describe("Basic tests")
print(name_in_str("Across the rivers", "chris"))					# ,True)
print(name_in_str("Next to a lake", "chris"))						# ,False)
print(name_in_str("Under a sea", "chris"))						# ,False)
print(name_in_str("A crew that boards the ship", "chris"))		# ,False)
print(name_in_str("A live son", "Allison"))						# ,False)
print(name_in_str("Just enough nice friends","Jennifer"))			# ,False)
print(name_in_str("thomas","Thomas"))								# ,True)
print(name_in_str("pippippi","Pippi"))							# ,True)
print(name_in_str("pipipp","Pippi"))								# ,False)
print(name_in_str("ppipip","Pippi"))								# ,False)

