# 对照示例：先写自己的程序并运行，再打开此文件。
text = input("请输入摄氏温度：")
celsius = float(text)
if celsius <= -273.15:
    print("温度超出本题允许的范围")
else:
    kelvin = celsius + 273.15
    print(f"{kelvin:.2f} K")
