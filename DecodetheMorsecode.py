MORSE_CODE = {".-":'a',"-...":'b',"-.-.":'c',"-..":'d',".":'e',"..-.":'f',"--.":'g',"....":'h',"..":'i',".---":'j',
"-.-":'k',".-..":'l',"--":'m',"-.":'n',"---":'o',".--.":'p',"--.-":'q',".-.":'r',"...":'s',"-":'t',"..-":'u',"...-":'v',
".--":'w',"-..-":'x',"-.--":'y',"--..":'z',".----":'1',"..---":'2',"...--":'3',"....-":'4',".....":'5',"-....":'6',
"--...":'7',"---..":'8',"----.":'9',"-----":'0',"":" ","...---...":'SOS',"-.-.--":'!',".-.-.-":'.'}
# SOS,!,. 另外寫在字典
# "":" " 辨別字之間隔

def decodeMorse(morse_code):
    # morse_code = morse_code.replace("   ","  ") #單字間的空格為1格，另一格做字串分割
    # morse_code = morse_code.strip("  ") #去頭尾多餘空格
    # morse_code = morse_code.split(" ") #字串分割
    morse_code = ((morse_code.replace("   ","  ")).strip("  ")).split(" ") #前三行的整合

    result = "" #空白字串
    
    for i in morse_code:
        result += MORSE_CODE[i] #解碼
    return result.upper() #轉大寫

# ==========================mhadam, AhmetTuncel=============================
# def decodeMorse(morseCode):

#     morseCode = morseCode.strip().replace("   ", " * ") #用星號決定是否加字之間的空格 Amazing~

#     msg = ""
    
#     for x in morseCode.split():
#         if x != "*":
#             msg += MORSE_CODE[x]
#         else:
#             msg += " "
    
#     return msg
# ==========================================================================

# 測試
# def test_and_print(got, expected):
#     if got == expected:
#         test.expect(True)
#     else:
#         print("<pre style='display:inline'>Got {}, expected {}</pre>".format(got, expected))
#         test.expect(False)

# test.describe("Example from description")
print(decodeMorse('.... . -.--   .--- ..- -.. .'))			#, 'HEY JUDE')
print(decodeMorse('...---...'))                             #, 'SOS')
print(decodeMorse('.   .'))                                 #, 'E E')
print(decodeMorse('...   ---   ...'))                       #, 'S O S')
print(decodeMorse(' . '))                                   #, 'E')
print(decodeMorse('   .   . '))                             #, 'E E'
print(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))                                        #, 'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.'
