from tkinter import * # 导入库
from tkinter import messagebox
import ArchivalProcessing as AP
import Model as M
import sys
import platform as P
import time as t
from Page import *
from COMAPANY import random_keys
import os
from ProGressBar import ProGressBar
import threading
import queue as q
import random
from datetime import datetime

messagebox.showwarning('注意', '本游戏内所有公司名均为虚构!\n如有雷同 纯属巧合!')

def SelfCheck(): # 自建系统要求
    system_name = P.system()
    if not system_name == 'Windows':
        messagebox.showerror('Oops!', '本程序仅支持Windows系统!\n')
        sys.exit()
    AP.CheckTheTableOfContents()
    AP.ReadArchives()

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

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.job_queue = q.Queue()
    
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
        self.root.after(10, self.AllLabelUpdate)

    def MainInterface(self): # 主界面
        Version = Label(self.root, text = 'Versions: BETA.1.1', font = ('微软雅黑', 11))
        MoneyLabel = Label(self.root, text = f'你的钱: {M.Money}元', textvariable = self.MoneyVAR, font = ('微软雅黑', 14))
        WorkLabel = Label(self.root, text = f'工作单位: {M.Work}', textvariable = self.WorkVAR, font = ('微软雅黑', 14))

        LogButton = Button(self.root, text = '日志', command = self.Log, font = ('微软雅黑', 14))
        OpenMarketButton = Button(self.root, text = '自己开公司!', command = self.NC, font = ('微软雅黑', 14)) # 还未开放功能
        RecruitmentMarketButton = Button(self.root, text = '招聘市场', command = self.RecruitmentMarket, font = ('微软雅黑', 14))
        DoOddJobButton = Button(self.root, text = '打零工', command = self.DoOddJob, font = ('微软雅黑', 14))
        ShopButton = Button(self.root, text = '商店', command = self.GoToMarket, font = ('微软雅黑', 14))
        SMButton = Button(self.root, text = '说明', command = self.SM, font = ('微软雅黑', 14))

        MoneyLabel.pack() # 钱数
        WorkLabel.pack() # 工作单位
        Version.place(x = 660, y = 570) # 版本号

        ShopButton.pack() # 商店
        DoOddJobButton.pack() # 打零工
        RecruitmentMarketButton.pack() # 招聘市场
        LogButton.pack() # 日志
        SMButton.pack() # 说明

    def DoOddJob(self): # 打零工
        self.JOB = Tk()
        self.JOB.title('打零工')
        self.JOB.geometry('600x400')
        self.JOB.resizable(False, False)
        
        Label(self.JOB, text = '选择一个工作', font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '送外卖(10元/8秒)', command = lambda : self.AddOfOddJob('送外卖'), font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '快递驿站分拣(20元/16秒)', command = lambda : self.AddOfOddJob('快递驿站分拣'), font = ('微软雅黑', 14)).pack()
        Button(self.JOB, text = '送快递(30元/24秒)', command = lambda : self.AddOfOddJob('送快递'), font = ('微软雅黑', 14)).pack()
        
    def AddOfOddJob(self, job): # 打零工处理
        def job_thread():
            job_Seconds = {
                '送外卖' : 8,
                '快递驿站分拣' : 16,
                '送快递' : 24,
            }
            duration = job_Seconds.get(job, 8)  # 默认为8秒，如果没有找到对应的工作类型
            ProGress = ProGressBar(duration)
            ProGress.Run()
            if job == '送外卖': M.Money += 10
            elif job == '快递驿站分拣': M.Money += 20
            elif job == '送快递': M.Money += 30
            self.job_queue.put('job_done')

        threading.Thread(target=job_thread).start()

    def BuyItem(self, item, entry): # 购买物品处理
        if item == '小面包':
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

        Label(self.Market, text = '食品', font = ('微软雅黑', 20)).place(x = 50, y = 15)
        Label(self.Market, text = '小面包', font = ('微软雅黑', 13)).place(x = 53, y = 70)
        testbutton = Button(self.Market, text = '购买小面包(2元/个)', command = lambda: self.BuyItem('小面包', testentry))
        testlabel = Label(self.Market, text = '买多少个?')
        testentry = Entry(self.Market)
        testbutton.place(x = 30, y = 100)
        testlabel.place(x = 54, y = 130)
        testentry.place(x = 20, y = 150)

    def RecruitmentMarket(self): # 招聘市场
        self.DojOptions = {"default": "no", "icon": "info"}
        if M.Work != '无':
            a = messagebox.askquestion('tips', '你已经有工作了!\n想被老板炒鱿鱼啊!', **self.DojOptions)
            if a == 'no':
                messagebox.showinfo('tips', '算你识相!')
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
            button_text = f'{company}:{salary}元/现实一天'
            Button(self.RM, text=button_text, command=lambda c=company, s=salary : self.JoinCompany(c, s)).pack()

    def JoinCompany(self, company, salary): # 加入公司
        if M.Work == '无':
            if company not in self.PAGE_COMPANY_AND_DOLLAR:
                messagebox.showinfo('Tips', '这个公司不存在')
            else:
                messagebox.showinfo('TIps', f'你加入了{company}! 你将会每现实一天就会获得{salary}元!')
                M.Work = company
                M.LastSignInDate = datetime.now().date()
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
        Label(self.sm, text = '如果对本游戏觉得还不错的话, 请给我一个star吧! 真的感谢!').pack()
        Label(self.sm, text = 'https://github.com/meme123b/XPP-Shop', font = ('微软雅黑', 10)).pack()
        Label(self.sm, text = '制作者——WuBinBang').pack()

    def Log(self): # 日志
        self.log = Tk()
        self.log.title('日志')
        self.log.geometry('1000x400')
        self.log.resizable(False, False)

        TitleText = Label(self.log, text = '---日志信息---', font = ('微软雅黑', 17))
        
        BETA1_0 = Label(self.log, text = 'BETA1.0: 基本框架完成 开始制作游戏玩法', font = ('微软雅黑', 12))
        BETA1_1 = Label(self.log, text = 'BETA1.1: 打零工更新 加入"说明"按钮', font = ('微软雅黑', 12))
        BETA1_2 = Label(self.log, text = 'BETA2.0: 1、优化代码  2、日志内部"未来的计划"项去除  3、招聘市场更新  4、签到功能更新  5、解决一些已知问题', font = ('微软雅黑', 12))

        TitleText.pack()
        BETA1_0.pack()
        BETA1_1.pack()
        BETA1_2.pack()

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
        self.root.mainloop()

if __name__ == '__main__': # 运行
    Main().Run()
