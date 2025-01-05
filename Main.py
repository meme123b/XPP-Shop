from tkinter import *
from tkinter import messagebox
import ArchivalProcessing as AP
import Model as M
import sys
import platform as P
import time as t
from datetime import datetime
from Page import *
from COMAPANY import random_keys
import os

messagebox.showwarning('注意', '本游戏内所有公司名均为虚构!\n如有雷同 纯属巧合!')

def SelfCheck():
    system_name = P.system()
    if not system_name == 'Windows':
        messagebox.showerror('出错了!', '本程序仅支持Windows系统!\n')
        sys.exit()
    AP.CheckTheTableOfContents()
    AP.ReadArchives()

SelfCheck()

class Main:
    def __init__(self):
        self.PAGE_COMPANY_AND_DOLLAR = comapany_Dict

        self.root = Tk()
        self.root.title('XPP生活')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        self.MoneyVAR = StringVar()
        self.WorkVAR = StringVar()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def on_closing(self):
        MESSAGE = messagebox.askquestion('提示', '保存并退出？')
        if MESSAGE == 'yes':
            AP.SaveArchives()
            sys.exit()
        else:
            MESSAGE2 = messagebox.askquestion('提示', '不保存并退出？')
            if MESSAGE2 == 'yes':
                sys.exit()
    
    def AllLabelUpdate(self):
        self.MoneyVAR.set(f'你的钱: {M.Money}元')
        self.WorkVAR.set(f'工作单位: {M.Work}')
        self.root.after(10, self.AllLabelUpdate)

    def MainInterface(self):
        Version = Label(self.root, text = 'Versions: BETA.1.0', font = ('微软雅黑', 11))
        MoneyLabel = Label(self.root, text = f'你的钱: {M.Money}元', textvariable = self.MoneyVAR, font = ('微软雅黑', 14))
        WorkLabel = Label(self.root, text = f'工作单位: {M.Work}', textvariable = self.WorkVAR, font = ('微软雅黑', 14))

        LogButton = Button(self.root, text = '日志', command = self.NC, font = ('微软雅黑', 14)) # 还未开放功能
        OpenMarketButton = Button(self.root, text = '自己做生意!', command = self.NC, font = ('微软雅黑', 14)) # 还未开放功能
        RecruitmentMarketButton = Button(self.root, text = '招聘市场', command = self.RecruitmentMarket, font = ('微软雅黑', 14))
        DoOddJobButton = Button(self.root, text = '打零工', command = self.DoOddJob, font = ('微软雅黑', 14))
        ShopButton = Button(self.root, text = '商店', command = self.GoToMarket, font = ('微软雅黑', 14))

        MoneyLabel.pack() # 钱数
        WorkLabel.pack() # 工作单位
        Version.place(x = 660, y = 570) # 版本号

        ShopButton.pack() # 商店
        DoOddJobButton.pack() # 打零工
        RecruitmentMarketButton.pack() # 招聘市场
        LogButton.pack() # 日志

    def DoOddJob(self):
        self.DojOptions = {"default": "no", "icon": "info"}
        if M.Work != '无':
            a = messagebox.askquestion('tips', '你已经有工作了!\n想被老板炒鱿鱼啊!', **self.DojOptions)
            if a == 'no':
                messagebox.showinfo('tips', '算你识相!')
                return None
            else:
                messagebox.showinfo('tips', '你被炒鱿鱼了!')
                M.Work = '无'

        self.JOB = Tk()
        self.JOB.title('打零工')
        self.JOB.geometry('600x400')
        self.JOB.resizable(False, False)
        
    def BuyItem(self, item, entry):
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

    def GoToMarket(self):
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

    def RecruitmentMarket(self):
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

    def Log(self):
        self.log = Tk()
        self.log.title('日志')
        self.log.geometry('600x400')
        self.log.resizable(False, False)

        LogText = Label(self.log, text = '---日志信息---', font = ('微软雅黑', 13))
        LogText.pack()

        self.log.mainloop()

    def NC(self):
        messagebox.showinfo('提示', '此功能尚未开放!\n\n请耐心等待通知!')

    def Run(self):
        self.MainInterface()
        self.AllLabelUpdate()
        self.root.mainloop()

Main().Run()
