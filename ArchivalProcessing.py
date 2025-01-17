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
            f.write(f"{Windows_user_name}\nNone\n100")
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
    with open(path, 'r', encoding = 'utf-8') as f:
        for i in f.read().splitlines():
            List.append(i)
        f.close()
    M.UserName = List[0]
    M.Work = List[1]
    if M.Work == 'None':
        M.Work = '无'
    else:
        M.Work = List[1]
    M.Money = int(List[2])
    try:
        M.LastSignInDate = List[3]
    except:
        M.LastSignInDate = datetime.now().date()
    messagebox.showinfo('提示', f'存档加载完成!\n\n欢迎回来!{M.UserName}')
    return List

def SaveArchives():
    global path
    with open(path, 'w', encoding = 'utf-8') as f:
        f.truncate()
        if(M.Work == '无'):
            M.Work = 'None'
        f.write(f"{M.UserName}\n{M.Work}\n{M.Money}\n{M.LastSignInDate}")
        f.close()
