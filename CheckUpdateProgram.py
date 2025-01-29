from tkinter import messagebox
import urllib.request
import json
import Model as M
import os
import sys
import threading

def download_and_extract(url, extract_to='.'):
    # 下载文件
    filename = url.split('/')[-1]
    with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
        data = response.read()  # 读取数据
        out_file.write(data)  # 写入文件


def update_application():
    try:
        # 获取最新版本的下载链接
        response = urllib.request.urlopen('https://api.github.com/repos/meme123b/XPP-Shop/releases/latest')
        html = response.read().decode('utf-8')
        latest_release = json.loads(html)
        download_url = latest_release['assets'][0]['browser_download_url']  # 假设第一个资产是 zip 文件

        # 下载并解压新版本
        download_and_extract(download_url, extract_to='.')

        # 显示版本详情
        version_details = latest_release['body']
        messagebox.showinfo('版本详情', f'下载完成!版本详情:\n{latest_release["tag_name"]}\n\n{version_details}')
        
        messagebox.showinfo('Complete', '已完成!你可以删除此旧版本程序玩新版本了!')

    except Exception as e:
        messagebox.showerror('错误', f'更新过程中发生错误: {e}')

def CheckUpdate():
    try:
        with urllib.request.urlopen('https://api.github.com/repos/meme123b/XPP-Shop/releases/latest') as response:
            html = response.read().decode('utf-8')
            latest_release = json.loads(html)
            latest_version = latest_release['tag_name']
            current_version = M.Version
            if latest_version != current_version:
                if messagebox.askquestion('更新', f'发现新版本: {latest_version}\n 按下"确定"以下载并安装更新!\n注:游戏所在目录一定是要有写入权限的!也要保证有良好的网络环境!') == 'yes':
                    messagebox.showinfo('更新', '关闭此界面开始更新!\n你还可以继续玩你的游戏!\n注:下载完成后要自行删除旧版本文件!')
                    threading.Thread(target=update_application).start()
                else:
                    return None
            else:
                messagebox.showinfo('更新', '当前已是最新版本。')
    except urllib.error.URLError as e:
        messagebox.showerror('错误', f'检查更新时发生错误: {e}')
    except json.JSONDecodeError as e:
        messagebox.showerror('错误', f'解析更新信息时发生错误: {e}')
