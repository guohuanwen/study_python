#!/usr/bin/python 
#-*-coding:utf-8

"""
请计算 19+2*4-8/2
"""
a = 19+2*4-8/2
print (a)



'''

'''
print "你好，世界";
a = 2;
if a == 1:
	print "true";
else :
	print "false";
	
#raw_input("\n\npress the enter key to exit");
a,b,c=1,2,"guohuanwen";
print a,b,c;
print c[2:4]*2;
#list
list = [1,2,"guo",12.34,"huanwen"];
print list;
#元组（不能二次赋值）
tuple = ("and",1,"d");
print tuple;
dictionary = {'guo':"huan","wen":"gu"};
print dictionary;
print dictionary["guo"];
print dictionary.keys();
print dictionary.values


def dd():
	i = 0;

dd()


'''
布尔运算
'''
a = False
b = True
print (a and b)
print (a or b)
print (not(a and b))
if a :
    print ("a=True")
else :
    print ("a=False")


c = 5
if c == 1:
    print ("1")
elif c == 2:
    print ("2")
elif c == 3:
    print ("3")
else :
    print ("其他")



print ("请输入任意一个整数数字")
'''
#通过raw_input()输入数字是字符串
#用int()将字符串转化为整数
'''
number = int(input()) 
if number >50:
    print ("您输入的数字%d大于50,%d"%(number,number))
elif number == 50:
    print ("您输入的数等于50")
else :
    print ("您属于的数%d小于50"%number)


url = "github.com"
print (url[2])
print (url[2:4])
print (url[3:])
print (url[:3])
print (url[-3])

my_list = [1,2,3,4,5]
print (my_list[2])
print (my_list[2:])
print (my_list[-2])
print("\n--list中添加一个数 my_list.append(23)")
my_list.append(23)
print (my_list[5])
print("\n--list 长度 length = len(my_list)")
length = len(my_list)
print("\n--在list后添加一个数 my_list[length:] = [21]")
my_list[length:] = [21]
print (my_list)
print("\n--在list首部添加一个数 my_list[:0] = [21]")
my_list[:0] = [21]
print (my_list)
print("\n--扩充list  add_list = [2222,3333]  my_list.extend(add_list)")
add_list = [2222,3333]
my_list.extend(add_list)
text = "qwer";
my_list.extend(text)
print(add_list)
print(my_list)
print("\n--某元素出现的次数 print(my_list.count(4))")
my_list.extend(my_list)
print(my_list)
print(my_list.count(4))
print("\n元素在list中的位置  my_list.index(4)  存在多个 取第一个元素的位置")
print (my_list.index(4))

print("\nrange(0,-9,-1) 返回list 0:开始值 -9:结束值  -1步长")
llist = []
llist = range(0,-9,-1)
print(llist)
print(help(range))



'''
    def 函数名（参数1，参数2...）:
        函数体
'''
def add_function(a,b):
    c = a + b
    print(c)

if __name__=="__main__":
    add_function(1,2)










