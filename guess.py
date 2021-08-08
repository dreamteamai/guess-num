# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要各素他 比答案大/小

import random
start = input('決定隨機數字開始值')
end = input('決定隨機數字結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = input('猜一個1~100的數字')
	num = int(num)
	if num == r:
		print('猜對了')
		print('這是你猜的第', count, '次')
		break
	else:
		if num > r:
			print('比答案大')
		elif num < r:
			print('比答案小')
	print('這是你猜的第', count, '次')		