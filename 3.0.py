#V3.0

#主菜单
#平面图形
#立体图形
#二级菜单（平面）
#面积
#周长
#二级菜单（立体）
#立方体
#球体
#圆锥体
#圆柱体
#三级菜单（面积）
#矩形
#三角形
#圆形
#三级菜单（周长）
#矩形
#三角形
#圆形

#增加计算图形
#增加计算种类
#优化了代码结构

import math

def juxing_mianji(chang,kuan):
    """矩形面积"""
    try:
        chang = float(input("请输入长:"))
        kuan = float(input("请输入宽:"))
        mianji = chang * kuan
        return mianji
    except:
        print("请输入有效的数字!")

def sanjiaoxing_mianji(di,gao):
    """三角形面积"""
    try:
        di = float(input("请输入底:"))
        gao = float(input("请输入高:"))
        sanjiaoxin = di * gao / 2
        return sanjiaoxin
    except:
        print("请输入有效的数字!")

def yuanxing_mianji(banjin):
    """圆形面积"""
    try:
        banjin = float(input("请输入半径:"))
        mianji = math.pi * banjin ** 2
        return mianji
    except:
        print("请输入有效的数字!")

def juxing_zhouchang(chang,kuan):
    """矩形周长"""
    try:
        chang = float(input("请输入长:"))
        kaun = float(input("请输入宽:"))
        zhouchang = (chang + kuan) * 2
        return zhouchang
    except:
        print("请输入有效的数字!")

def sanjiaoxing_zhouchang(bian1,bian2,bian3):
    """三角形周长"""
    try:
        bian1 = float(input("请输入第一个边长:"))
        bian2 = float(input("请输入第二个边长:"))
        bian3 = float(input("请输入第三个边长:"))
        zhouchang = (bian1 + bian2 + bian3)
        return zhouchang
    except:
        print("请输入有效的数字!")

def yuanxing_zhouchang(banjin):
    """圆形周长"""
    try:
        banjin = float(input("请输入半径:"))
        zhouchang = math.pi * banjin * 2
        return zhouchang
    except:
        print("请输入有效的数字!")

def lifangti_tiji(chang,kuan,gao):
    """立方体体积"""
    try:
        chang = float(input("请输入长:"))
        kuan = float(input("请输入宽:"))
        gao = float(input("请输入高:"))
        tiji = chang*kuan*gao
        return tiji
    except:
        print("请输入有效的数字！")

def qiuti_tiji(banjin):
    """球体体积"""
    try:
        banjin = float(input("请输入半径:"))
        tiji = 4/3 * math.pi * banjin ** 3
        return tiji
    except:
        print("请输入有效的数字!")

def yuanzhui_tiji(banjin,gao):
    """圆锥体积"""
    try:
        banjin = float(input("请输入半径:"))
        gao = float(input("请输入高:"))
        tiji = math.pi * banjin ** 2 * gao / 3
        return tiji
    except:
        print("请输入有效的数字!")

def yuanzhu_tiji(banjin,gao):
    """圆柱体积"""
    try:
        banjin = float(input("请输入半径:"))
        gao = float(input("请输入高:"))
        tiji = math.pi * banjin ** 2 * gao
        return tiji
    except:
        print("请输入有效的数字!")


def menu():
    """主菜单"""
    print("\n===面积体积计算器===")
    print("1.平面图形")
    print("2.立体图形")
    print("3，退出程序")
    print("=====================")

def menu_2_1():
    """二级菜单,平面"""
    print("----------------")
    print("1.面积")
    print("2.周长")
    print("3.返回")
    print("-----------------")

def menu_2_2():
    """二级菜单,立体"""
    print("----------------")
    print("1.立方体")
    print("2.球体")
    print("3.圆锥体")
    print("4.圆柱体")
    print("5.返回")
    print("----------------")

def menu_3_1():
    """三级菜单,面积"""
    print("----------------")
    print("1.矩形")
    print("2.三角形")
    print("3.圆形")
    print("4.返回")
    print("----------------")

def menu_3_2():
    """三级菜单，周长"""
    print("----------------")
    print("1.矩形")
    print("2.三角形")
    print("3.圆形")
    print("4.返回")
    print("----------------")

def main():
    """主程序"""
    while True:
        menu()
        choice = input("请选择操作:")
        if choice == "1":
            while True:
                menu_2_1()
                choice_2_1 = input("请选择操作:")
                if choice_2_1 == "1":
                    while True:
                        menu_3_1()
                        choice_3_1 = input("请选择操作:")
                        if choice_3_1 == "1":
                            print(f"面积为:{juxing_mianji("请输入长:","请输入宽:")}")
                        elif choice_3_1 == "2":
                            print(f"面积为:{sanjiaoxing_mianji("请输入底:","请输入高:")}")
                        elif choice_3_1 == "3":
                            print(f"面积为:{yuanxing_mianji("请输入半径:")}")
                        elif choice_3_1 == "4":
                            break
                elif choice_2_1 == "2":
                    while True:
                        menu_3_2()
                        choice_3_2 = input("请选择操作:")
                        if choice_3_2 == "1":
                            print(f"周长为:{juxing_zhouchang("请输入长:","请输入宽:")}")
                        elif choice_3_2 == "2":
                            print(f"周长为:{sanjiaoxing_zhouchang("请输入第一个边长:","请输入第二个边长:","请输入第三个边长:")}")
                        elif choice_3_2 == "3":
                            print(f"周长为:{yuanxing_zhouchang("请输入半径:")}")
                        elif choice_3_2 == "4":
                            break
                elif choice_2_1 == "3":
                    break
        elif choice == "2":
            while True:
                menu_2_2()
                choice_2_2 = input("请选择操作:")
                if choice_2_2 == "1":
                    print(f"体积为:{lifangti_tiji("请输入长:","请输入宽:","请输入高:")}")
                elif choice_2_2 == "2":
                    print(f"体积为:{qiuti_tiji("请输入半径:")}")
                elif choice_2_2 == "3":
                    print(f"体积为:{yuanzhui_tiji("请输入半径:","请输入高:")}")
                elif choice_2_2 == "4":
                    print(f"体积为:{yuanzhu_tiji("请输入半径:","请输入高:")}")
                elif choice_2_2 == "5":
                    break
        elif choice == "3":
           print("感谢您使用本计算器！")
           break
        else:
            print("无效的选择，请重新输入！")

if __name__ == "__main__":
    main()