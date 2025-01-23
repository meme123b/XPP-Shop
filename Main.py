from tkinter import * # 导入库
from tkinter import messagebox
import ArchivalProcessing as AP
import Model as M
import sys
import platform as P
import time as t
from Page import *
import os
from ProGressBar import ProGressBar
import threading
import queue as q
import random
from datetime import datetime
from CheckUpdateProgram import CheckUpdate

messagebox.showwarning('注意', '本游戏内所有公司名均为虚构!\n如有雷同 纯属巧合!')

def SelfCheck(): # 自建系统要求
    system_name = P.system()
    if not system_name == 'Windows':
        messagebox.showerror('Oops!', '本程序仅支持Windows系统!\n')
        sys.exit()
    AP.CheckTheTableOfContents()
    AP.ReadArchives()
    ReallyVersion = 'v3.0b'
    M.Version = 'v3.0b'

SelfCheck() # 调用自建系统要求方法

class Main: # 主程序
    def __init__(self): # 初始化
        self.PAGE_COMPANY_AND_DOLLAR = comapany_Dict

        self.root = Tk()
        self.root.title('XPP生活')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        self.MoneyVAR = StringVar()
        self.WorkVAR = StringVar()
        self.EducationalBackgroundVAR = StringVar()

        self.BreadsVAR = StringVar()
        self.WaterVAR = StringVar()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.job_queue = q.Queue()
        self.learn_queue = q.Queue()
    
    def on_closing(self): # 关闭窗口时
        MESSAGE = messagebox.askquestion('提示', '保存并退出？')
        if MESSAGE == 'yes':
            AP.SaveArchives()
            sys.exit()
        else:
            MESSAGE2 = messagebox.askquestion('提示', '不保存并退出？')
            if MESSAGE2 == 'yes':
                sys.exit()
    
    def AllLabelUpdate(self): # 更新所有文本标签
        self.MoneyVAR.set(f'你的钱: {M.Money}元')
        self.WorkVAR.set(f'工作单位: {M.Work}')
        self.EducationalBackgroundVAR.set(f'学历值: {M.Learn}')
        self.BreadsVAR.set(f'小面包有 {M.Breads} 个')
        self.WaterVAR.set(f'水娃娃矿泉水有 {M.Water} 瓶')
        self.root.after(10, self.AllLabelUpdate)

    def MainInterface(self): # 主界面
        Version = Label(self.root, text = 'Versions: BETA.3.0', font = ('微软雅黑', 11))
        MoneyLabel = Label(self.root, text = f'你的钱: {M.Money}元', textvariable = self.MoneyVAR, font = ('微软雅黑', 14))
        EducationalBackgroundLabel = Label(self.root, text = f'学历值:{M.Learn}', textvariable = self.EducationalBackgroundVAR, font = ('微软雅黑', 14))
        WorkLabel = Label(self.root, text = f'工作单位: {M.Work}', textvariable = self.WorkVAR, font = ('微软雅黑', 14))

        LogButton = Button(self.root, text = '日志', command = self.Log, font = ('微软雅黑', 14))
        RecruitmentMarketButton = Button(self.root, text = '招聘市场', command = self.RecruitmentMarket, font = ('微软雅黑', 14))
        DoOddJobButton = Button(self.root, text = '打零工', command = self.DoOddJob, font = ('微软雅黑', 14))
        ShopButton = Button(self.root, text = '商店', command = self.GoToMarket, font = ('微软雅黑', 14))
        BagButton = Button(self.root, text = '背包', command = self.Bag, font = ('微软雅黑', 14))
        GoToLearnButton = Button(self.root, text = '去学习', command = self.GoToLearn, font = ('微软雅黑', 14))
        SMButton = Button(self.root, text = '说明', command = self.SM, font = ('微软雅黑', 14))
        CheckUpdateButton = Button(self.root, text = '检查可用更新', command = CheckUpdate, font = ('微软雅黑', 11))

        MoneyLabel.pack() # 钱数
        EducationalBackgroundLabel.pack() # 学历值
        WorkLabel.pack() # 工作单位
        Version.place(x = 660, y = 570) # 版本号

        ShopButton.pack() # 商店
        BagButton.pack() # 背包
        DoOddJobButton.pack() # 打零工
        GoToLearnButton.pack() # 去学习
        RecruitmentMarketButton.pack() # 招聘市场
        LogButton.pack() # 日志
        SMButton.pack() # 说明
        CheckUpdateButton.place(x = 550, y = 565) # 检查更新

    def Bag(self): # 背包
        BagItemsDict = {
            '小面包' : M.Breads,
            '水娃娃矿泉水' : M.Water,
        }
        self.bag = Tk()
        self.bag.title('背包')
        self.bag.geometry('600x400')
        self.bag.resizable(False, False)
        Label(self.bag, text = '--背包--', font = ('微软雅黑', 15)).pack()
        Label(self.bag, text = '由于作者太菜 背包的刷新数量功能没有做\n要刷新得重新打开背包界面awa', font = ('微软雅黑', 15)).pack()
        Label(self.bag, text = '', font = ('微软雅黑', 10)).pack()
        Label(self.bag, text = f'小面包有 {BagItemsDict["小面包"]} 个', textvariable = self.BreadsVAR, font = ('微软雅黑', 14)).pack()
        Label(self.bag, text = f'水娃娃矿泉水有 {BagItemsDict["水娃娃矿泉水"]} 瓶', textvariable = self.WaterVAR, font = ('微软雅黑', 14)).pack()

    def AddOfLearn(self, learn): # 学习处理
        def learn_thread():
            learn_Seconds = {
                '自学' : 2,
                '补习班' : 10,
                '九年丽星教育' : 60
            }
            learn_Money = {
                '自学' : 0,
                '补习班' : 100,
                '九年丽星教育' : 1000
            }
            if learn_Money[learn] > M.Money:
                messagebox.showinfo('提示', 'Bro钱不够啊!')
                return None
            
            if learn == '补习班': M.Money -= 100
            elif learn == '九年丽星教育': M.Money -= 1000

            duration = learn_Seconds.get(learn)
            ProGress = ProGressBar(duration)
            ProGress.Run()
            if learn == '自学': M.Learn += 1
            elif learn == '补习班': M.Learn += 2
            elif learn == '九年丽星教育': M.Learn += 30
            self.learn_queue.put('learn done')

        threading.Thread(target = learn_thread).start()

    def GoToLearn(self):
        self.learn = Tk()
        self.learn.title('学习')
        self.learn.geometry('600x400')
        self.learn.resizable(False, False)

        Label(self.learn, text = '选择一个学习方式', font = ('微软雅黑', 14)).pack()
        Button(self.learn, text = '自学(免费/2秒)+1学历', command = lambda : self.AddOfLearn('自学'), font = ('微软雅黑', 14)).pack()
        Button(self.learn, text = '补习班(100元/10秒)+2学历', command = lambda : self.AddOfLearn('补习班'), font = ('微软雅黑', 14)).pack()
        Button(self.learn, text = '重新开启九年丽星教育(1000元/60秒)+30学历', command = lambda : self.AddOfLearn('九年丽星教育'), font = ('微软雅黑', 14)).pack()

    def DoOddJob(self): # 打零工
        self.JOB = Tk()
        self.JOB.title('打零工')
        self.JOB.geometry('600x400')
        self.JOB.resizable(False, False)
        
        Label(self.JOB, text = '选择一个工作', font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '送外卖(10元/8秒)', command = lambda : self.AddOfOddJob('送外卖'), font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '快递驿站分拣(20元/16秒)', command = lambda : self.AddOfOddJob('快递驿站分拣'), font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '送快递(30元/24秒)', command = lambda : self.AddOfOddJob('送快递'), font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '去XX奶茶店打工(30元/24秒)', command = lambda : self.AddOfOddJob('去XX奶茶店打工'), font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '做网站审核员(10元/8秒)', command = lambda : self.AddOfOddJob('做网站审核员'), font = ('微软雅黑', 14)).pack()
        
    def AddOfOddJob(self, job): # 打零工处理
        def job_thread():
            job_Seconds = {
                '送外卖' : 8,
                '快递驿站分拣' : 16,
                '送快递' : 24,
                '去XX奶茶店打工' : 24,
                '做网站审核员' : 8
            }
            duration = job_Seconds.get(job, 8)  # 默认为8秒，如果没有找到对应的工作类型
            ProGress = ProGressBar(duration)
            ProGress.Run()
            if job == '送外卖': M.Money += 10
            elif job == '快递驿站分拣': M.Money += 20
            elif job == '送快递': M.Money += 30
            elif job == '去XX奶茶店打工': M.Money += 30
            elif job == '做网站审核员': M.Money += 10
            self.job_queue.put('job_done')

        threading.Thread(target=job_thread).start()

    def BuyItem(self, item, entry): # 购买物品处理
        if item == '小面包' or item == '水娃娃矿泉水':
            BUY = 2
            try:
                num = int(entry.get())
            except:
                messagebox.showinfo('tips', '请输入一个整数!')
                return None
        
        num = int(entry.get())
        if num > 0:
            question = messagebox.askquestion('购买', f'你确定要购买{num}个{item}吗?\n一共需要{num * BUY}元')
            if question == 'yes':
                if M.Money >= num * BUY:
                    M.Money -= num * BUY
                    messagebox.showinfo('tips', f'购买成功!你那清纯的背包被你塞下了{num}个{item}!')
                    if item == '小面包': M.Breads += num
                    elif item == '水娃娃矿泉水': M.Water += num
                else:
                    messagebox.showinfo('tips', '钱不够awa!')
            else:
                messagebox.showinfo('tips', '已放弃支付!')
                return None
        else:
            messagebox.showinfo('tips', '请输入一个大于0的正整数!')
            return None

    def GoToMarket(self): # 商店
        self.Market = Tk()
        self.Market.title('商店')
        self.Market.geometry('800x600')
        self.Market.resizable(False, False)

        Label(self.Market, text = '食品', font = ('微软雅黑', 20)).place(x = 63, y = 15)

        Label(self.Market, text = '小面包', font = ('微软雅黑', 13)).place(x = 66, y = 70)
        BuyBreadbutton = Button(self.Market, text = '购买小面包(2元/个)', command = lambda: self.BuyItem('小面包', BuyBreadentry))
        BuyBreadlabel = Label(self.Market, text = '买多少个?')
        BuyBreadentry = Entry(self.Market)
        BuyBreadbutton.place(x = 43, y = 100)
        BuyBreadlabel.place(x = 67, y = 130)
        BuyBreadentry.place(x = 33, y = 150)

        Label(self.Market, text = '水娃娃矿泉水', font = ('微软雅黑', 13)).place(x = 50, y = 200)
        BuyWaterbutton = Button(self.Market, text = '购买水娃娃矿泉水(2元/瓶)', command = lambda: self.BuyItem('水娃娃矿泉水', BuyWaterentry))
        BuyWaterlabel = Label(self.Market, text = '买多少瓶?')
        BuyWaterentry = Entry(self.Market)
        BuyWaterbutton.place(x = 30, y = 230)
        BuyWaterlabel.place(x = 69, y = 260)
        BuyWaterentry.place(x = 33, y = 280)

        Label(self.Market, text = 'Other', font = ('微软雅黑', 20)).place(x = 400, y = 15)
        Label(self.Market, text = '还没想好!', font = ('微软雅黑', 13)).place(x = 403, y = 70)

    def RecruitmentMarket(self): # 招聘市场
        self.DojOptions = {"default": "no", "icon": "info"}
        if M.Work != '无':
            a = messagebox.askquestion('tips', '你已经有工作了!\n想被老板炒鱿鱼啊!', **self.DojOptions)
            if a == 'no':
                return None
            else:
                messagebox.showinfo('tips', '你被炒鱿鱼了!')
                M.Work = '无'

        self.RM = Tk()
        self.RM.title('招聘市场')
        self.RM.geometry('800x600')
        self.RM.resizable(False, False)
        
        # 将字典项转换为列表，然后随机选择几个公司
        selected_companies = random.sample(list(self.PAGE_COMPANY_AND_DOLLAR.items()), 5)  # 随机选择5家公司
        for i, (company, salary) in enumerate(selected_companies, start=1):
            button_text = f'{company}:{salary}元/现实一天\n要求学历:{EducationalBackgroundDict[company]}'
            Button(self.RM, text=button_text, command=lambda c=company, s=salary : self.JoinCompany(c, s)).pack()

    def JoinCompany(self, company, salary): # 加入公司
        self.JoinCompanyOptions = {"default": "yes", "icon": "info"}
        if M.Work == '无':
            if company not in self.PAGE_COMPANY_AND_DOLLAR:
                messagebox.showinfo('Tips', '这个公司不存在')
            else:
                if M.Learn >= EducationalBackgroundDict[company]:
                    messagebox.showinfo('Tips', f'你加入了{company}! 你将会每现实一天就会获得{salary}元!')
                    M.Work = company
                    M.LastSignInDate = datetime.now().date()
                else:
                    messagebox.askquestion('Tips', 'Bro学历太垃了吧 快点去学习吧!\n菜鸡!', **self.JoinCompanyOptions)
        else:
            messagebox.showinfo('Tips', '你已经有一个工作了!')
            return None

    def SM(self): # 说明
        self.sm = Tk()
        self.sm.title('说明')
        self.sm.resizable(False, False)
        Label(self.sm, text = 'XPP Shop', font = ('微软雅黑', 20)).pack()
        Label(self.sm, text = '这是一个打工赚钱小游戏', font = ('微软雅黑', 10)).pack()
        Label(self.sm, text = '虽然这个游戏没有反作弊 但最好还是别用作弊道具 不然就不好玩了', font = ('微软雅黑', 10)).pack()
        Label(self.sm, text = '')
        Label(self.sm, text = '如果对本游戏觉得还不错的话, 请给我一个star吧! 真的感谢!', font = ('微软雅黑', 10)).pack()
        Label(self.sm, text = 'https://github.com/meme123b/XPP-Shop', font = ('微软雅黑', 10)).pack()
        Label(self.sm, text = '如果发现更新错误或者是bug, 请在github上或者在我的邮箱(13705894451@163.com)上告诉我!你的支持是我最大的动力!', font = ('微软雅黑', 10)).pack()
        Label(self.sm, text = '制作者——WuBinBang').pack()

    def Log(self): # 日志
        self.log = Tk()
        self.log.title('日志')
        self.log.geometry('1000x400')
        self.log.resizable(False, False)

        TitleText = Label(self.log, text = '---日志信息---', font = ('微软雅黑', 17))
        
        BETA1_0 = Label(self.log, text = 'BETA1.0: 基本框架完成 开始制作游戏玩法', font = ('微软雅黑', 12))
        BETA1_1 = Label(self.log, text = 'BETA1.1: 打零工更新 加入"说明"按钮', font = ('微软雅黑', 12))
        BETA2_0 = Label(self.log, text = 'BETA2.0: 1、优化代码  2、日志内部"未来的计划"项去除  3、招聘市场更新  4、签到功能更新  5、解决一些已知问题', font = ('微软雅黑', 12))
        BETA2_1 = Label(self.log, text = 'BETA2.1: 1、优化代码  2、完成自动更新功能', font = ('微软雅黑', 12))
        BETA2_2 = Label(self.log, text = 'BETA2.2: 1、增加打零工内容  2、增加商店内商品数', font = ('微软雅黑', 12))
        BETA2_3 = Label(self.log, text = 'BETA2.3: 1、改进更新  2、修复已知bug', font = ('微软雅黑', 12))
        BETA3_0 = Label(self.log, text = 'BETA3.0: 1、加入学历及相关内容  2、进入公司条件更新  3、更新模块大体完成  4、背包更新  5、读取存档大改进', font = ('微软雅黑', 12))
        WarningText = Label(self.log, text = '\n注:从2.0版本开始 写入文件编码为UTF-8 而之前的是GBK所以旧版本已经扫不了存档了\n如果使用旧版本exe(BETA1.0~BETA1.1)打开会出错\n而且如果是新版本存档然后又打开了旧版本exe(BETA1.0~BETA1.1)的 是会导致部分数据丢失!', font = ('微软雅黑', 15))

        TitleText.pack()
        BETA1_0.pack()
        BETA1_1.pack()
        BETA2_0.pack()
        BETA2_1.pack()
        BETA2_2.pack()
        BETA2_3.pack()
        BETA3_0.pack()
        WarningText.pack()

        self.log.mainloop()
    
    def check_sign_in(self): # 签到函数
        current_date = str(datetime.now().date())
        
        if (current_date != M.LastSignInDate) and (M.Work != '无'):
            print(current_date)
            print(M.LastSignInDate)
            M.LastSignInDate = current_date

            salary = self.PAGE_COMPANY_AND_DOLLAR.get(M.Work, 0)
            M.Money += salary
            messagebox.showinfo('tips', f'你的工资入账了!为{salary}元!')

    def NC(self): # 无功能函数
        messagebox.showinfo('提示', '此功能尚未开放!\n\n请耐心等待通知!')

    def Run(self): # 运行函数
        self.MainInterface()
        self.AllLabelUpdate()
        self.check_sign_in()
        threading.Thread(target = CheckUpdate).start()
        self.root.mainloop()

if __name__ == '__main__': # 运行
    Main().Run()
