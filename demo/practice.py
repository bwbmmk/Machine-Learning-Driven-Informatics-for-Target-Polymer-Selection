import time
print('-----聚合物教学数据之python练习小程序-----\n---------------hello python---------------')
name = input('请输入名字\n>')
while 1:
    temp = int(input('please input the temperature\n>'))
    unit = input('please input the unit(C or K)\n>')
    print('checking...')
    time.sleep(1)
    match unit:#判断温度单位书写是否正确，以及摄氏度转开尔文，并判断开尔文温度的范围正确性
        case  'K' | 'k':
            if float(temp)<=0:#判断开尔文温度是否超出范围
                print('your temperature is impossible!!')
            else:
                time.sleep(1)
                print('OK,I konw!')
                break
        case 'C'|'c':
            print('yeah,you are ok! But I will convert it to the unit \'k\'')
            temp=float(temp)+273.15
            if float(temp)<=0:#判断开尔文温度是否超出范围
                print('your temperature is impossible!!')
            else:
                time.sleep(1)
                print('OK,I konw!')
                break
        case _:
            print('wrong input!')

dict = {'ID': 'A01', 'NAME': name, 'TEMP': temp, 'UNIT': unit}
time.sleep(1)
print(dict)
time.sleep(1)
#一段并无太大意义的输出
print('so,id:{}({}) is {:.2f} {} now!'.format(dict['ID'], dict['NAME'], dict['TEMP'], 'K'))
