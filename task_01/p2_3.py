# p2_3.py
temp = input("猜一下我想的是哪个数字？")
guess = int(temp)
while guess != 8 :
    if guess < 8:
        guess = int(input('小了小了,重新试试'))
    else:
        guess = int(input('大了大了,重新试试'))
print('哈哈，你是我心里的蛔虫么？')
