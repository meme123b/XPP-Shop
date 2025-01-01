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

now = datetime.now()


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
        RecruitmentMarketButton = Button(self.root, text = '招聘市场', command = self.RecruitmentMarket, font = ('微软雅黑', 14))
        ShopButton = Button(self.root, text = '商店', command = self.GoToMarket, font = ('微软雅黑', 14))

        MoneyLabel.pack() # 钱数
        WorkLabel.pack() # 工作单位
        Version.place(x = 660, y = 570) # 版本号

        ShopButton.pack() # 商店
        RecruitmentMarketButton.pack() # 招聘市场
        LogButton.pack() # 日志

    def GoToMarket(self):
        self.NC()

    def RecruitmentMarket(self):
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
