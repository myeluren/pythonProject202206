# # 定义车票变量
# # 定义刀的长度
has_ticket = True
knife_length = 30
# 有车票可以进入，没有车票不能入内
# 刀的长度不能超过20cm
if has_ticket:
    print("检票通过")
    if knife_length <= 20:
        print("安检通过，请入内")
    else:
        print("危险！危险！刀的长度为 %d ，不允许入内" % knife_length)
else:
    print("请买票")

# if has_ticket:
#     print("入内")
# elif knife_length >= 232:
#     print("刀不错")
# else:
#     print("拜拜")
