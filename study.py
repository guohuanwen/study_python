#!/usr/bin/python 
#-*-coding:utf-8

"""
����� 19+2*4-8/2
"""
a = 19+2*4-8/2
print (a)



'''

'''
print "��ã�����";
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
#Ԫ�飨���ܶ��θ�ֵ��
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
��������
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
    print ("����")



print ("����������һ����������")
'''
#ͨ��raw_input()�����������ַ���
#��int()���ַ���ת��Ϊ����
'''
number = int(input()) 
if number >50:
    print ("�����������%d����50,%d"%(number,number))
elif number == 50:
    print ("�������������50")
else :
    print ("�����ڵ���%dС��50"%number)


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
print("\n--list�����һ���� my_list.append(23)")
my_list.append(23)
print (my_list[5])
print("\n--list ���� length = len(my_list)")
length = len(my_list)
print("\n--��list�����һ���� my_list[length:] = [21]")
my_list[length:] = [21]
print (my_list)
print("\n--��list�ײ����һ���� my_list[:0] = [21]")
my_list[:0] = [21]
print (my_list)
print("\n--����list  add_list = [2222,3333]  my_list.extend(add_list)")
add_list = [2222,3333]
my_list.extend(add_list)
text = "qwer";
my_list.extend(text)
print(add_list)
print(my_list)
print("\n--ĳԪ�س��ֵĴ��� print(my_list.count(4))")
my_list.extend(my_list)
print(my_list)
print(my_list.count(4))
print("\nԪ����list�е�λ��  my_list.index(4)  ���ڶ�� ȡ��һ��Ԫ�ص�λ��")
print (my_list.index(4))

print("\nrange(0,-9,-1) ����list 0:��ʼֵ -9:����ֵ  -1����")
llist = []
llist = range(0,-9,-1)
print(llist)
print(help(range))



'''
    def ������������1������2...��:
        ������
'''
def add_function(a,b):
    c = a + b
    print(c)

if __name__=="__main__":
    add_function(1,2)










