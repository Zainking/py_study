# p2_4.py
import random

temp = input("猜一下我想的是哪个数字？")
guess = int(temp)
secret = random.randint(1, 10)

while guess != secret :
    if guess < secret:
        guess = int(input('小了小了,重新试试'))
    else:
        guess = int(input('大了大了,重新试试'))
print('哈哈，你是我心里的蛔虫么？')
