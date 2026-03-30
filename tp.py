import time
import threading
import random
a = 0
游戏继续 = True
空格计数 = 0
时间 = 0
空格数 = 0
摔倒 = 1
摔倒显示 = 0

def 敌人():
    global a,游戏继续,时间,摔倒,摔倒显示
    a = 20
    b = 20
    while 游戏继续:
        # 限制范围
        if 摔倒 != 100:
            摔倒 = random.randint(1,100)
        if a > b: 
            a = b
        if a < 0:
            a = 0
        c = a * " "
        if 摔倒显示 > 0 and 摔倒 == 100:
            print("😱你还倒着先起来😱")
        if 摔倒 != 100:
            摔倒显示 = 0    
        print('\033c',end = '')  
        if 摔倒 == 100:
            print(f"😵{c}😈")
            print("你摔倒了😭输入1")
        elif a >= 15:    
            print(f"🥺{c}😈")
        elif a >= 10:   
            print(f"😱{c}😈")
        elif a == 0:
            print("😭被抓住了🥺")   
            游戏继续 = False
            break 
        else:
            print(f"😭{c}😈")
        if 空格数 != 0:
            print(f"🔥你跑了{空格数}格")
        time.sleep(0.3)    
        a -= 1
        时间 += 0.3
def 输入检查():
    global a,空格计数,空格数,摔倒,摔倒显示
    while 游戏继续:
        cc = input("")
        if not 游戏继续:
            break
        空格数 = cc.count(' ')
        摔倒起来 = cc.count('1')
        if 摔倒起来 > 0:
            摔倒 = 1
        if 空格数 > 0 and 摔倒 != 100:
            print(f"🔥你跑了{空格数}格")  
            a += 空格数 
            空格计数 += 空格数
        elif 空格数 > 0 and 摔倒 == 100:
            print("😱你还倒着先起来😱")   
            摔倒显示 = 20 
        else:
            continue
def 开始游戏():
    global 游戏继续
    print('按空格帮助🥺逃离😈')
    print('注意是按空格后按回车可以按多个空格再按回车')
    print('摔倒了🥺输入1站起来')
    time.sleep(5)
    
    显示 = threading.Thread(target = 敌人)
    输入 = threading.Thread(target = 输入检查)
    显示.start() 
    输入.start()
    显示.join()
    输入.join()
    print(f"🥺坚持了{时间}秒🔥")
    print(f"🔥你一共按了{空格计数}次空格🔥")
#空格帮助🥺逃跑    
开始游戏()    