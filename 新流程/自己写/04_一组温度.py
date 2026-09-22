# 04 一组温度
# 先看 ../任务卡/04_一组温度.md；从下一行开始亲手写。
for temp in [25, 50, -20]:
    temp_k = float(temp) + 273.15
    if temp_k <= 0:
        print('your temperature is impossible!!')
    else:
        print('{:.2f}k'.format(temp_k))