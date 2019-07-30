def make_readable(seconds):
    if seconds<60 and seconds>=0:
        S=seconds
        M=H=0
    if seconds<3600 and seconds>=60:
        M=seconds//60
        S=seconds%60
        H=0
    if seconds>=3600:
        H=seconds//3600
        M=(seconds%3600)/60
        S=seconds%60
    return ("%02d" % H)+":"+("%02d" % M)+":"+("%02d" % S) #02代表兩位，%H為小時補滿兩位

# 測試======================================
# print(make_readable(0)) 		#, "00:00:00")
# print(make_readable(5)) 		#, "00:00:05")
# print(make_readable(60))		#, "00:01:00")
# print(make_readable(86399)) 	#, "23:59:59")
print(make_readable(359999))	#, "99:59:59")