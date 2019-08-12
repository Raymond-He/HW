# ===================================邱寶=================================
def score(dice):
    buf_sum=[]
    point={'trione':1000,'six':600,'trifive':500,'four':400,'three':300,'two':200,'one':100,'five':50}
    for i in range(1,7):
        dice_num = dice.count(i) #1~7 出現次數
        if dice.count(i) == 4:
            if i == 1:
                buf_sum.append(point['one']) #丟一次100到buf_sum
            elif i == 5:
                buf_sum.append(point['five']) #印一次50到buf_sum
            dice_num = dice.count(i)-1 #出現剩3次

        if dice.count(i) == 5:
            if i == 1:
                buf_sum.append(point['one'])
                buf_sum.append(point['one'])
            elif i == 5:
                buf_sum.append(point['five'])
                buf_sum.append(point['five'])
            dice_num = dice.count(i)-2 #出現剩3次

        if dice_num == 3: #出現3次
            if i == 1:
                buf_sum.append(point['trione'])
            elif i == 2:
                buf_sum.append(point['two'])
            elif i == 3:
                buf_sum.append(point['three'])
            elif i == 4:
                buf_sum.append(point['four'])
            elif i == 5:
                buf_sum.append(point['trifive'])
            elif i == 6:
                buf_sum.append(point['six'])

        if dice_num == 1: #出現一次
            if i == 1:
                buf_sum.append(point['one'])
            
            elif i == 5:
                buf_sum.append(point['five'])
        
        if dice_num == 2: #出現二次
            if i == 1:
                buf_sum.append(point['one'])
                buf_sum.append(point['one'])
            
            elif i == 5:
                buf_sum.append(point['five'])
                buf_sum.append(point['five'])

    return sum(buf_sum) #buf_sum內總和

# 測試
# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings
# test.describe("Example Tests")
# test.it("Example Case")
print( score( [2, 3, 4, 6, 2] ))           #, 0)
print( score(  [4, 4, 4, 3, 3] ))          #, 400)
print( score(  [2, 4, 4, 5, 4] ))          #, 450)
print( score(  [1, 1, 1, 1, 1] ))          #, 1200)

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
