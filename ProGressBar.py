import tkinter as tk
from tkinter import ttk

class ProGressBar():
    def __init__(self):
        self.GOBACKHOME = 'NO'
        self.PB = tk.Tk()
        self.PB.title('工作')
        self.PB.geometry('300x100')
        self.PB.resizable(False, False)
        self.PROGRESSCOMPLETEVAR = tk.StringVar()
        LABELBAR = tk.Label(self.PB, text = '', textvariable = self.PROGRESSCOMPLETEVAR, font = ('微软雅黑', 14))
        LABELBAR.pack()
        self.PROGRESSCOMPLETEVAR.set('--正在努力工作中--')
        self.progressbar = ttk.Progressbar(self.PB, orient='horizontal', length=200, mode='determinate')
        self.progressbar.pack(pady=20)

    def start_progress(self):
        self.progressbar['value'] = 0
        self.update_progress(0)

    def update_progress(self, step):
        if step < 101:
            self.progressbar['value'] = step
            self.PB.after(50, self.update_progress, step + 1)
        else:
            self.PROGRESSCOMPLETEVAR.set('--完成--')
            self.PB.after(1000, self.PB.destroy)
            self.GOBACKHOME = 'OK'

    def on_closing(self):
        self.GOBACKHOME = 'NO'
        self.PB.destroy()

    def Run(self):
        self.start_progress()
        self.PB.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.PB.mainloop()
        if self.GOBACKHOME == 'OK':
            return 'MONEY'
        else:
            return '扣工资'
