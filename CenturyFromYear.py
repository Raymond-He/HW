def century(year):
    if year<100: #one centry equal 100 years
        return 1
    else:
        if year%100 != 0:
            return int(year//100)+1
        else:
            return int(year//100)


# 測試
print(century(1705))          # , 18, 'Testing for year 1705')
print(century(1900))          # , 19, 'Testing for year 1900')
print(century(1601))          # , 17, 'Testing for year 1601')
print(century(2000))          # , 20, 'Testing for year 2000')
print(century(356))           # , 4, 'Testing for year 356')
print(century(89))            # , 1, 'Testing for year 89')