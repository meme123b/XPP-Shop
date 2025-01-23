import os
import sys
import Model as M
from time import sleep
from tkinter import *
from tkinter import messagebox
import subprocess as s
from datetime import datetime

Windows_user_name = os.getlogin()

LogPath = ''
for i in range(len(__file__) - 21):
    LogPath += __file__[i] #ProGram File: ArchivalProcessing.py

path = 'C:/Users/Administrator/AppData/LocalLow/XPPGame/Archive.sav'

def CheckTheTableOfContents():
    global path, Windows_user_name
    # 检查目录是否存在
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        # 目录不存在，创建目录
        os.makedirs(directory)

    # 检查文件是否存在
    if not os.path.exists(path):
        # 文件不存在，创建并写入内容
        with open(path, 'w') as f:
            f.write(f"{Windows_user_name}\nNone\n100\n{datetime.now().date()}\nv3.0b\n0")
            f.close()

def Draw_Text(Text = '', SleepTime = 0, endl = False) -> None:
    for i in Text:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(SleepTime)
    if endl:
       print()

def ReadArchives():
    global path
    List = []
    with open(path, 'r', encoding='utf-8') as f:
        for i in f.read().splitlines():
            List.append(i)
        f.close()

    # 读取用户名
    M.UserName = List[0] if len(List) > 0 else '默认用户名'

    # 读取工作
    M.Work = List[1] if len(List) > 1 else '无'
    if M.Work == 'None':
        M.Work = '无'

    # 读取金钱
    M.Money = int(List[2]) if len(List) > 2 else 0

    # 读取最后签到日期
    M.LastSignInDate = List[3] if len(List) > 3 else datetime.now().date()

    # 读取版本
    M.Version = List[4] if len(List) > 4 else 'v3.0b'

    # 读取学习时间
    M.Learn = int(List[5]) if len(List) > 5 else 0

    # 读取面包数量
    M.Breads = int(List[6]) if len(List) > 6 else 0

    # 读取水数量
    M.Water = int(List[7]) if len(List) > 7 else 0

    messagebox.showinfo('提示', f'存档加载完成!\n\n欢迎回来!{M.UserName}')
    return List

def SaveArchives():
    global path
    with open(path, 'w', encoding = 'utf-8') as f:
        f.truncate()
        if(M.Work == '无'):
            M.Work = 'None'
        f.write(f"{M.UserName}\n{M.Work}\n{M.Money}\n{M.LastSignInDate}\n{M.Version}\n{M.Learn}\n{M.Breads}\n{M.Water}")
        f.close()
