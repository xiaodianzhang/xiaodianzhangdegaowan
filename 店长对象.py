class ggb:
    类型 = "干尸"
    总店长数 = 0
    def __init__(self,名字,年龄):
        self.__密码 = 97183114514
        self.__hp = 3
        self.年龄 = 年龄
        self.名字 = 名字
        self.棍母 = ["棍母"]
        ggb.总店长数 += 1
        print(f"名为{名字}的店长被创建了😋")
        print(f"现在有{ggb.总店长数}个店长")
    def 棍母列表(self,要添加的东西):
        self.棍母.append(要添加的东西)
    def 移除指定棍母(self,棍母名):
        if 棍母名 in self.棍母:
            self.棍母.remove(棍母名)
            print(f"{棍母名}被删除了😱")
        else:
            print(f"未找到{棍母名}🥺")
    def 移除全部棍母(self):
        try:
            self.棍母.clear()
            print("棍母们被移除了😭") 
        except:
            print("移除失败了🤨")
    def 查看hp(self,密码):
        if 密码 == self.__密码:
            print(self.__hp)
        else:
            print("错误😡")             
店长信息 = ggb("店长",1145)
print("店长年龄=",店长信息.年龄)
print("店长是啥=",店长信息.类型)
print("店长的棍母列表里有",店长信息.棍母)
店长信息.棍母列表("滚木")
print("店长的棍母列表内现在有",店长信息.棍母)
店长信息.移除指定棍母("棍母")
print("店长的棍母列表内现在有",店长信息.棍母)
店长信息.移除全部棍母()

小店长信息 = ggb("小店长",13)
堕化店长信息 = ggb("堕化店长",114514)
print(ggb.总店长数) 

class ccb(ggb):
    类型 = "硬干尸"
    def __init__(self,名字,年龄):
        super().__init__(名字,年龄)
        print("但是这个店长更硬！")
ccb("大店长",777)

店长信息.查看hp(123456)  


店长信息.查看hp(97183114514)