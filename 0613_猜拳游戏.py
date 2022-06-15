import random

# 从控制台输入要出的拳头（石头-1，剪刀-2，布-3）
player = int(input("请出拳（石头-1，剪刀-2，布-3）："))
# 电脑随机出拳（默认出石头）
computer = random.randint(1, 5)
print("玩家出拳的是 %d - 电脑出拳是 %d" % (player, computer))
# 比较胜负
if player > computer:
    print("玩家胜利啦！")
elif player == computer:
    print("打成平手，再来一次！！！")
elif player < computer:
    print("电脑胜利啦！")
