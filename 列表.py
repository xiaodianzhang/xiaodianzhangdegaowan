def 斯大林排序(a):
    #该排序会是降序,他会把不符合规律的东西给删除
    长度 = len(a)
    i = 1
    while i < 长度:
        b = a[i - 1]
        if a[i] > b:
            a.remove(a[i])
            i -= 1
            长度 -= 1
        i += 1    
    return a        
def 不排序(a):
    return a            
b = [2,1,3,6,4,5]            
c = 不排序(b)            
for m in c:
    print(m,end= "")          
print()      
    
    
    
    
def 朱元璋排序(a):
    长度 = len(a)
    i = 1
    while i < 长度:
        b = a[i - 1]
        if a[i] > b:
            a = []
            return a
        i += 1
            
b = [2,1,3,6,4,5]            
c = 朱元璋排序(b)            
for m in c:
    print(m)          
print()            
            
b = [2,1,3,6,4,5]            
c = 斯大林排序(b)            
for m in c:
    print(m)
    
def 空气(a):
    #该排序会是降序，他会把不符合规律的东西给变为💨
    长度 = len(a)
    i = 1
    b = 0
    c = []
    while i < 长度:
        if a[b] == "💨":
            b += 1 
        elif a[i] > a[b]:
            a[i] = "💨"
            b -= 1
        i += 1
        b += 1    
    return a      
b = [2,1,3,6,4,5]            
c = 空气(b)            
for m in c:
    print(m,end= "")
    
    
    
def 反复排序(a):
    #该排序会反复在升序和降序中切换
    #如果你给的列表里的东西是奇数最后会返回升序的结果，偶数就是降
    长度 = len(a)
    b = []
    c = []
    停止 = True
    升 = False
    i = 0
    while i < 长度:
        b.append(a[i])
        b长 = len(b)
        if b长 < 2:
            pass
        elif 升 == False:
            for l in range(1,b长):
                j = 0
                while j < l:
                    if b[l] > b[j]:
                        b[l],b[j] = b[j],b[l]
                        j -= 1
                    j += 1    
            升 = True        
        else: 
            for l in range(1,b长):
                j = 0
                while j < l:
                    if b[l] < b[j]:
                        b[l],b[j] = b[j],b[l]
                        j -= 1
                    j += 1    
            升 = False    
        i += 1   
    return b    
        
print("\n")        
b = [2,1,3,6,4,5,7,8]            
c = 反复排序(b)            
for m in c:
    print(m,end= "")
    
def 淘汰(a):
    #升序#好吧其实是个选择
    i = 0
    j = 0
    b = []
    长度 = len(a)
    while 长度 != 0:
        if i == 0:
            目前最小 = a[i]
            目前最小的位置 = i
        elif a[i] < 目前最小:
            目前最小 = a[i]
            目前最小的位置 = i
        j += 1
        i += 1
        if j == 长度:
            j = 0
            长度 -= 1    
            i = 0
            b.append(a[目前最小的位置])
            a.remove(a[目前最小的位置])
    return b        
print("\n")        
b = [2,1,3,6,4,5,7,8]            
c = 淘汰(b)            
for m in c:
    print(m,end= "")            
            
def 同化(a):
    长 = len(a)
    i = 1
    while i < 长:
        if a[i] < a[i - 1]:
            a[i] = a[i - 1]
        i += 1
    return a        
            
print("\n")        
b = [2,1,3,6,4,5,7,8]            
c = 同化(b)            
for m in c:
    print(m,end= "")
    
def 我也不知道是啥排序(a):
    长 = len(a)    
    i = 1
    c = []  
    while i < 长:
        b = []
        重复几次 = a[i - 1]
        for _ in range(0,重复几次):
            b.append("a")
        c.append(len(b))    
        i += 1
    return 淘汰(c)
print("\n")        
b = [2,1,3,6,4,5,7,8]            
c = 我也不知道是啥排序(b)            
for m in c:
    print(m,end= "")       
    
def 也是反复排序(a):
    #这个函数会反复使用反复排序函数使用次数取决于你列表
    长 = len(a)
    for _ in range(0,长):
        a = 反复排序(a)
    return a    

print("\n")        
b = [2,1,3,6,4,5,7,8]            
c = 也是反复排序(b)            
for m in c:
    print(m,end= "")      
def 变大变高(a):
    a = 淘汰(a)
    长 = len(a)
    i = 0
    b = []
    while i < 长:    
        c = a[i]
        for _ in range(0,c):
            b.append(a[i])
        i += 1    
    return b 
    
print("\n")        
b = [2,1,3,6,4,5,7,8]            
c = 变大变高(b)            
for m in c:
    print(m,end= "")         
        