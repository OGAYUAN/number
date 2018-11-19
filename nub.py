#產生一個數隨機整數1~100(不要列印)
#讓使用者重複猜數字
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小
#在第幾次猜對的
import random
r = random.randint(1,100)
x = 0
print(r)
while True:
	x = x +1
	usre = input('請猜數字: ')
	usre = int(usre)
	if usre == r:
		print('終於猜對了')
		print('總共猜了', x, '次')
		break
	else:
		if r > usre:
			print('比答案小')
		elif r < usre:
			print('比答案大')
			



