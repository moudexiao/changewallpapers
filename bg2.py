import os
import random
import ctypes

wallpapers = []

# 遍历D:\Wallpaper文件夹下所有jpg文件名放入列表
for root, dirs, files in os.walk(r"D:\Pictures\wallpapers"):
    for f in files:
        temp = os.path.splitext(f)[1]
        if temp == ".jpg" or temp == ".png":
            wallpapers.append(os.path.join(root, f))

# 列表中随机选一个
choose = wallpapers[random.randint(0, len(wallpapers) - 1)]
# 更换选中的壁纸
ctypes.windll.user32.SystemParametersInfoW(20, 0, choose, 0)

