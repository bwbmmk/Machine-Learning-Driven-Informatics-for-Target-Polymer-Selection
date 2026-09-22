# 对照示例：先写自己的程序并运行，再打开此文件。
text = input("请输入摄氏温度：")
try:
    celsius = float(text)
except ValueError:
    print("请输入数字")
else:
    if celsius <= -273.15:
        print("温度超出本题允许的范围")
    else:
        print(f"{celsius + 273.15:.2f} K")
