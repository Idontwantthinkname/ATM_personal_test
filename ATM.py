money = 5000000
name = input("请输入你的姓名: ")


def Balance(show_header):
    """
    Balance: 余额
    :return: 返回None
    """
    if show_header:
        print("-------------------------------余额------------------------------")
    print(f"{name}，您好，您的余额剩余：{money}。")


def Deposit():
    """
    Deposit: 存款
    :return: 返回None
    """
    print("-------------------------------存款------------------------------")
    money_in = int(input("请输入存款金额"))
    print(f"{name}，您好，您存款{money_in}元成功。")
    global money
    money += money_in
    Balance(False)


def Withdraw():
    """
    Withdraw: 取款
    :return: 返回None
    """
    print("-------------------------------取款------------------------------")
    global money
    money_out = int(input("请输入取款金额"))

    if money_out <= money:
        print(f"{name}，您好，您取款{money_out}元成功。")
        money -= money_out
        Balance(False)
    else:
        print("您的余额不足。")
        Balance(False)


def main_menu():
    """
        main_menu: 主菜单
        :return: 结束程序
        """
    print("------------------------------主菜单------------------------------")
    print(f"{name}，您好，欢迎来到ATM，请选择你的操作。")
    print("查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")
    return input("请输入您的选择:\n")


while True:
    keyboard_input = main_menu()
    if keyboard_input == "1":
        Balance(True)
        continue
    elif keyboard_input == "2":
        Deposit()
        continue
    elif keyboard_input == "3":
        Withdraw()
        continue
    else:
        print("程序退出")
    break  # 通过break退出程序
