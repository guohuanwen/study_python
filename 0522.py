#encoding:UTF-8
from PIL import Image
import os,sys


##   图片转字符画


def image_tanslate(imagepath,filepath):
    ww = 100
    img = Image.open(imagepath)
    #转黑白
    img = img.convert('L') 
    width,height = img.size
    rate = width/ww
    width = int(ww)
    height = int(height/rate)
    print (width)
    print (height)
    img = img.resize((width,height))
    pix = img.load()
    ttxt = open(filepath,"w")
    aa = ""
    for h in range(0,height,1):
        for w in range(0,width,1):
            st = string_replace(pix[w,h])
            ttxt.write(st)
            aa = aa + st
            if w == ww-1:
                ttxt.write("\n")
                print(aa)
                aa = ""
                
    
    '''
    for w in range(0,width,1):
        for h in range(0,height,1):
            st = string_replace(pix[w,h])
            ttxt.write(st)
            aa = aa + st
            if h == height-1:
                ttxt.write("\n")
                print(aa)
                aa = ""
       '''         

    ttxt.close

    
def string_replace(number):
    param = 50
    n = int(number/param)
    j = int(255/param)
    s = "1234567890@#￥%&*qwertyuiop[]\asdfghjklzxcvbnm<>?/"
    for i in range(0,j,1):
        if (n == i):
            return s[n]
    return ".";
    

if __name__ == "__main__":
    imagepath="C:/Users/Administrator/Desktop/11.jpg"
    filepath = "C:/Users/Administrator/Desktop/zifu.txt"
    image_tanslate(imagepath,filepath)
