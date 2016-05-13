# encoding: utf-8


import os,sys,shutil
#正则的使用
import re

path = "C:\\Users\Administrator\Desktop";

#重装系统后，都是XXX快捷方式，写个脚本hahah
if __name__ == "__main__":
    names = os.listdir(path)
    for n in names:
        if re.search("-快捷方式",n):
            print(n)
            m = n.replace("-快捷方式","")
            os.rename(path+"\\"+n,path+"\\"+m)



