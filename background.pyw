import os
import random
import ctypes
import tkinter as tk
from tkinter import filedialog

#打开窗口获取文件夹路径
def open_folder_dialog():
    root = tk.Tk()
    root.withdraw()

    # 打开文件夹对话框
    dir_path = filedialog.askdirectory(title='请选择要换壁纸所在文件夹')

    # 获取文件夹绝对路径
    abs_path = os.path.abspath(dir_path)
    print(abs_path)
    return abs_path
def changewallpapers(wallpapers_directory):
    wallpapers = []
    # 遍历D:\Wallpaper文件夹下所有jpg文件名放入列表
    for root, dirs, files in os.walk(wallpapers_directory):
        for f in files:
            temp = os.path.splitext(f)[1]
            if temp == ".jpg" or temp == ".png":
                wallpapers.append(os.path.join(root, f))

    # 列表中随机选一个
    choose = wallpapers[random.randint(0, len(wallpapers) - 1)]
    # 更换选中的壁纸
    ctypes.windll.user32.SystemParametersInfoW(20, 0, choose, 0)

def function(file_path):

    if not os.path.exists(file_path):
        # 调用函数
        abs_path = open_folder_dialog()
        # 如果不存在，则创建文件
        with open(file_path, 'w') as f:
            f.write(abs_path) #写入内容

    wallpapers_directory = ''

    # 读取配置文件
    with open(file_path,'r') as f:
        wallpapers_directory = f.read().strip()
    return wallpapers_directory





if __name__=="__main__":
    # 获取当前目录
    dir_path = os.getcwd()
    # 检查目标文件是否存在
    file_path = os.path.join(dir_path, 'config.txt')
    wallpapers_directory =  function(file_path)
    if not os.path.exists(wallpapers_directory):
        print('error')
        os.remove(file_path)
        wallpapers_directory =  function(file_path)
    else:
        try:
            changewallpapers(wallpapers_directory)
        except:
            os.remove(file_path)





