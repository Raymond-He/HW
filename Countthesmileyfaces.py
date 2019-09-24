def count_smileys(arr):
    eyes = [':', ';']
    nose = ['','-','~']
    month = [')','D']
    face = []
    time = 0

    for i in eyes:
        for j in nose:
            for k in month:
                face.append(i+j+k)

    for x in arr:
        if x in face:
            time +=1
            
    return time

# 測試
# Test.describe("Basic tests")
print(count_smileys([]))									#, 0)
print(count_smileys([':D',':~)',';~D',':)']))				#, 4)
print(count_smileys([':)',':(',':D',':O',':;']))			#, 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))		#, 1)