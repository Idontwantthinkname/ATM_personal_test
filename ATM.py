money = 5000000
name = input("请输入你的姓名: ")


def Balance():
    """
    Balance: 余额
    :return: 返回None
    """
    print(f"{name}，您好，您的余额剩余：{money}")
    main_menu()


def Deposit():
    """
    Deposit: 存款
    :return: 返回None
    """
    money_in = int(input("请输入存款金额"))
    print(f"{name}，您好，您存款{money_in}元成功")
    global money
    money += money_in
    Balance()


def Withdraw():
    """
    Withdraw: 取款
    :return: 返回None
    """
    money_out = int(input("请输入取款金额"))
    global money
    if money_out <= money:
        print(f"{name}，您好，您取款{money_out}元成功")
        money -= money_out
        Balance()


def main_menu():
    """
    main_menu: 主菜单
    :return: 结束程序
    """
    print(f"{name}，您好，欢迎来到银行ATM，请选择你的操作")
    print("查询余额\t[输入1]\n存款\t\t[输入2]\n取款\t\t[输入3]\n退出\t\t[输入4]")
    num = int(input("请输入您的选择:\n"))

    if num == 1:
        Balance()

    if num == 2:
        Deposit()

    if num == 3:
        Withdraw()

    if num == 4:
        return None


main_menu()
