
    
        
最小值 = 1
最大值 = 100000
Q = 0
D = None
b = True
j = None
i = 0
N = 10
F = 0
print("选择4：得知目标数字是几位数  但是失去随机数最大值位数减目标数字位数的猜测次数\n--------------")
print("选择5：猜测次数=10000但提示变成🤪或其他")
c = input("选择1:可以多猜五次\n--------\n 选择2:得知目标数是奇数还是偶数\n-----------\n 选择3:失去4次猜测机会\n---------\n使范围的最小值乘以10最大值整除10向下取整\n--------\n")






























    
C = int(c)
if C == 5:
    print("🤪")
    F = 1
    N = 10000

if C == 3:
    最小值 *= 10
    最大值 //= 10
    N -= 4
    数字 = random.randint(最小值,最大值)
else:
    数字 = random.randint(最小值,最大值)
if C == 4:
    D = len(str(数字))
    print(f"目标数是{D}位数")
    d = len(str(最大值))
    M = d - D
    N -= M + 2
    print(f"失去了{M+2}次猜测次数")
    print(f"剩余{N}次猜测次数")
      
         
if C == 1:
    N += 5
    print("猜测次数成功变为",N)
if C == 2:
    if 数字 % 2 == 0:
        print("目标数是偶数")
        j = 2
    else:
        print("目标数是奇数")
        j = 1
if C == 114514917813:
    print("👁👁👁👁猜测👁99999")
    N = 99999
    Q = 1            
while b and i < N and Q != 1 and F != 1:
    a = input(f"猜{最小值}到{最大值}的数字")
    A = int(a)
    if j == 1 and A % 2 == 0:
        c = input("你确定嘛？目标数已经提示是偶数了确认请输入1否则按其他的来重新选择")
        C = int(c)
        if C != 1:
            continue 
    if j == 2 and A % 2 != 0:
        c = input("你确定嘛？目标数已经提示是奇数了确认请输入1否则按其他的")
        C = int(c)
        if C != 1:
            continue
    if A < 最小值 or A > 最大值:
        c = input("你确定吗？你选的数字不在范围里面，确定输入1不确定输入其他数字")
        C = int(c)
        if C == 2:
            continue
    if A > 数字:
        print("大了")
    elif A < 数字:
        print("小了")
    if A == 数字:
        print("✓")
        b = False
    i += 1
    print(f"你猜了{i}次还可以猜{N - i}次") 
while b and i < N and Q != 1 and F == 1:
    a = input(f"猜🤪到🤪的数字")
    A = int(a)
    if j == 1 and A % 2 == 0:
        c = input("你确定嘛？目标数已经提示是🤪了确认请输入1否则按其他的来重新选择")
        C = int(c)
        if C != 1:
            continue 
    if j == 2 and A % 2 != 0:
        c = input("你确定嘛？目标数已经提示是奇数了确认请输入1否则按其他的")
        C = int(c)
        if C != 1:
            continue
    if A < 最小值 or A > 最大值:
        c = input("你🤪吗？你选的🤪不🤪里面，确定输入🤪不确定输入🤪")
        C = int(c)
        if C == 2:
            continue
    if A > 数字:
        print("🤪")
    elif A < 数字:
        print("🥺")
    if A == 数字:
        print("✓")
        b = False
    i += 1
    print(f"你猜了🤪次还可以猜🥺次") 

    
    
while b and i < N and Q == 1:
    a = input("猜👁dao👁的数字")
    A = int(a)
    if A > 数字:
        print("👁👁")
    elif A < 数字:
        print("👁")
    if A == 数字:
        print("✓")
        b = False
    i += 1
    print(f"你猜了👁次还可以猜👁次") 
if b and Q == 1:
    print("👁👁👁👁👁👁👁👁👁👁👁👁👁👁👁")   
if b and Q != 1:
    print(f"你用光了全部的次数🤪随机数是{数字}") 