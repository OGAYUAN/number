#產生一個數隨機整數a~b(不要列印)
#讓使用者重複猜數字
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小
#在第幾次猜對的
#讓使用者決定範圍數
import random #載入
a = input('請輸入最小數: ')#使用者設定最大數
b = input('請輸入最大數: ')#使用者設定最小數
a = int( a )#記得類型轉換
b = int( b )#記得類型轉換
r = random.randint(a , b)
x = 0#啟示次數
print(r)
while True:
	x = x +1#猜一次+1
	usre = input('請猜數字: ')
	usre = int(usre)#記得類型轉換
	if usre == r:
		print('終於猜對了')
		print('總共猜了', x, '次')
		break#答對時結束
	else:
		if r > usre:
			print('比答案小')
		elif r < usre:
			print('比答案大')
			



