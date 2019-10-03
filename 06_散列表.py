# 创建一个散列表 python的实现方式为字典
book = dict()
book['apple'] = 0.62
book['mile'] = 3.5
book['test'] = '哈哈哈'

print(book['test'])

# 下面是一些实践

#  在python 中创建散列表的快捷方式就是一对大括号，千万别和其他语言混淆哦~
phone_book = {}


while True:
    select = input('增加联系人 1， 查找联系人 2 :\n')
    if select == '1':
        name = input('请输入联系人名称: ')
        tel = input('请输入联系人电话：')
        phone_book[name] = tel
        print('储存成功！')
    elif select == '2':
        s_name = input('请输入要查找的姓名：')
        if phone_book.get(s_name):
            print('%s的电话是：%s' %(s_name, phone_book[s_name]))
        else:
            up_tel = input('联系人不存在，增加联系人输入电话，退出请按q: ')
            if up_tel == 'q' : break
            phone_book[s_name] = up_tel
    else:
        print('输入错误')
        break

